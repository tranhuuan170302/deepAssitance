from typing import List, Tuple


def get_langgraph_tools(tool_manager, required_tools: List[str]) -> Tuple[List, str]:
    tools = []
    descriptions = []

    for name in required_tools:
        tool = tool_manager.get_tool(name)
        if tool:
            tools.append(tool)
            descriptions.append(tool_manager.generate_tool_prompt(tool))
    
    return tools, "\n".join(descriptions)


def get_all_langgraph_tools(tool_manager) -> Tuple[List, str]:
    tools = []
    descriptions = []

    for name, tool in tool_manager.tool_index.items():
        tools.append(tool)
        descriptions.append(tool_manager.generate_tool_prompt(tool))
    
    return tools, "\n".join(descriptions)