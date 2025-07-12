from langgraph.prebuilt import create_react_agent
from agent_service.tools.tool_manager import ToolManager
from agent_service import app_config, logger


def build_private_researcher_agent(tool_manager: ToolManager):
    """
        Build a private researcher agent. This agent is used to answer questions
        about the private researcher in Database (Neo4j and Qdrant).

        Parameters
        ----------
        tool_manager : ToolManager
            The tool manager to use for the agent.

        Returns
        -------
        Agent
            The private researcher agent.
    """
    required_tools = ["private_knowledge_mcp"]
    tools, descriptions = get_langgraph_tools(tool_manager, required_tools)

    return create_react_agent(
        get_llm_by_type(app_config.private_researcher_agent),
        tools,
        prompt=lambda state: apply_prompt_template(
            "private_researcher_agent_prompt", state, PromptType.AGENT, descriptions
        ),
        debug=False,
    )
