import re
from tkinter import constants
from typing import Dict, List, Optional

import httpx
from langchain_core.tools import BaseTool, StructuredTool, Tool, ToolException
from langchain_core.utils.function_calling import convert_to_openai_tool
from langchain_mcp_adapters.client import MultiServerMCPClient
from mcp.types import CallToolResult, EmbeddedResource, ImageContent, TextContent
from mcp.types import Tool as MCPTool
from pydantic import BaseModel, Field, create_model


NonTextContent = ImageContent | EmbeddedResource


class ToolManager:

    def __init__(self):
        self.tool_index = Dict[str, BaseTool] = {}
        self.function_specs: Dict[str, dict] = {}

    @staticmethod
    def _convert_call_tool_result(
            call_tool_result: CallToolResult
        ) -> tuple[str | list[str], list[NonTextContent] | None]:

        text_contents: list[NonTextContent] = []
        non_text_contents = []
        for content in call_tool_result.content:
            if isinstance(content, TextContent):
                text_contents.append(content)
            else:
                non_text_contents.append(content)

        tool_content: str | list[str] = [
            content.text for content in text_contents
        ]

        if len(text_contents) == 1:
            tool_content = tool_content[0]

        if call_tool_result.error:
            raise ToolException(call_tool_result.error)

        return tool_content, non_text_contents or None

    def convert_mcp_tool_to_langchain_tool(
        self,
        tool: MCPTool
    ) -> BaseTool:
        """
        Convert an MCP to a LangChain tool.

        Args:
            tool: The MCP tool to convert.

        Returns:
            A LangChain tool.
        """

        
        async def call_tool(
            **arguments: dict[str, Any]
        ) -> tuple[str | list[str], list[NonTextContent] | None]:
            url_central = f"http://{constants.CENTRAL_SERVER_URL}:{constants.CENTRAL_SERVER_PORT}/tool/run-tool/{tool.name}"
            payload = {
                "tool_name": tool.name,
                "arguments": arguments
            }
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    url_central,
                    json=payload
                )
                resp.raise_for_status()
                call_tool_result = resp.json().get("result")

            return _convert_call_tool_result(CallToolResult(**call_tool_result))
        
        return StructuredTool(
            name=tool.name,
            description=tool.description,
            args_schema=tool.inputSchema,
            coroutine=call_tool,
            response_format="content_and_artifact",
        )


    async def refresh_tools(self):

        try:
            enpoint_central_service_list_tools = f"""http://{constants.CENTRAL_SERVER_URL}:
                                                    {constants.CENTRAL_SERVER_PORT}/tool/list-tools"""
            async with httpx.AsyncClient(timeout=constants.HTTPX_TIMEOUT) as client:
                resp = await client.get(enpoint_central_service_list_tools)
                resp.raise_for_status()
                tools = resp.json().get("tools")
                for tool in tools:
                    self.tool_index[tool.name] = self.convert_mcp_tool_to_langchain_tool(tool)
        except Exception as e:
            logger.error(f"Failed to refresh tools: {e}")
            return


    def get_tool(self, name: str):
        return self.tool_index.get(name)

    def get_function_spec(self, name: str):
        return self.function_specs.get(name)

    def list_all_tools(self):
        return list(self.tool_index.values())

    def list_all_function_specs(self):
        return list(self.function_specs.values())

    def generate_tool_prompt(self, tool: StructuredTool) -> str:
        spec = convert_to_openai_tool(tool, strict=True)
        name = spec["function"]["name"]
        description = spec["function"]["description"]
        parameters = spec["function"]["parameters"]["properties"]

        arg_lines = []

        for arg, meta in parameters.items():
            line = f"- `{arg}` ({meta.get('type', 'description')})"
            if meta.get("required"):
                line += "-  **required**"
            arg_lines.append(line)

        return f""" ###
        {name} \n
        {description} \n
        Arguments:\n {arg_lines}
        """
