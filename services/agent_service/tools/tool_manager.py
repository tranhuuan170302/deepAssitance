import re
from typing import Dict, List, Optional

import httpx
from langchain_core.tools import BaseTool, StructuredTool, Tool, ToolException
from langchain_core.utils.function_calling import convert_to_openai_tool
from langchain_mcp_adapters.client import MultiServerMCPClient
from mcp.types import CallToolResult, EmbeddedResource, ImageContent, TextContent
from mcp.types import Tool as MCPTool
from pydantic import BaseModel, Field, create_model



class ToolManager:

    def __init__(self):
        self.tool_index = Dict[str, BaseTool] = {}
        self.function_specs: Dict[str, dict] = {}

    def _convert_call_tool_result(self, 
            call_tool_result: CallToolResult) -> tuple[str | list[str], list[NoneTextContent] | None]:

        text_contents: list[NoneTextContent] = []
        non_text_contents = []
        for content in call_tool_result.content:
            if isinstance(content, TextContent):
                text_contents.append(content)
            else:
                non_text_contents.append(content)
        
        tool_content: str | list[str] = [content.text for content in text_contents]
        if len(text_contents) == 1:
            tool_content = tool_content[0]
        
        if call_tool_result.error:
            raise ToolException(call_tool_result.error)
        
        return tool_content, non_text_contents or None
    
    def call_tool(self, ):
        pass

    def refresh_tools(self):
        pass

    def get_tool(self, name: str):
        pass

    def get_function_spec(self):
        pass

    def list_all_tools(self):
        pass

    def list_all_function_specs(self):
        pass

    def generate_tool_prompt(self):
        pass
    
        