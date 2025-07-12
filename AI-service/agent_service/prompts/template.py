import datetime
import os
from enum import Enum
from tkinter import SINGLE
from typing import Dict, List, Any


class PromptType(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"
    GROUP = "group_type"
    SINGLE = "single_type"
    ORCHESTRATOR = "orchestrator_type"

def get_prompt_template(prompt_name: str, prompt_type: PromptType) -> str:
    """
    Load a prompt template from a markdown file.

    Parameters
    ----------
    prompt_name : str
        The name of the prompt template to apply (without .md extension)
    prompt_type : PromptType
        The type of prompt to apply

    Returns
    -------
    str
        The prompt template string with placeholders
    """
    try:
        template_path = os.path.join(
            os.path.dirname(__file__), prompt_type.value, f"{prompt_name}.md"
        )
        with open(template_path, "r") as f:
            template = f.read()
        return template
    except FileNotFoundError:
        raise ValueError(f"Prompt template {prompt_name} not found")
    except Exception as e:
        raise ValueError(f"Failed to load prompt template {prompt_name}: {e}")


def apply_prompt_template(
    prompt_name: str,
    state: Dict[str, Any],
    prompt_type: PromptType,
    tool_description: str = "",
) -> List[Dict[str, str]]:
    """
    Apply a prompt template to the given state.

    Parameters
    ----------
    prompt_name : str
        The name of the prompt template to apply
    state : Dict[str, Any]
        The current state of the conversation or task
    prompt_type : PromptType
        The type of prompt to apply
    tool_description : str, optional
        A description of the tools available to the agent, by default ""

    Returns: List of message dictionaries with the system prompt added
    -------
    List[Dict[str, str]]
        A list of dictionaries containing the prompt template and any additional information
    """

    template = get_prompt_template(prompt_name, prompt_type)
    
    # Replace placeholders with value from state
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    template = template.replace("<<CURRENT_TIME>>", current_time)
    template = template.replace("<<TOOL_DESCRIPTION>>", tool_description)
    template = template.replace("<<USER_INPUT>>", state.get("user_input", ""))
    
    # create system message with the prompt
    system_message = {
        "role": "system",
        "content": template,
    }
    
    return [system_message] + state.get("messages", [])
