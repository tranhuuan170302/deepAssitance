from fastapi import APIRouter, Request

agent_router = APIRouter(tags=["single_agent"])

@agent_router.post("/coordinator")
async def invoke_coordinator(state: dict, request: Request):
    """
        Routes the current processing state to the appropriate agent.

        Parameters
        ----------
        state : dict
            A dictionary representing the current conversation or task state. It may include 
            keys such as 'user_input', 'retrieved_docs', or 'intermediate_results'.

        Returns
        -------
        str
            The identifier for the next agent to invoke, or 'END' to stop processing.

        Raises
        ------
        KeyError
            If expected keys are missing in the state.
        ValueError
            If no suitable agent is determined for the given state.

        Examples
        --------
        coordinator({'user_input': 'search for climate report'})
        'retrieval_agent'
    """
    pass


@agent_router.post("/planner")
async def invoke_planner(state: dict, request: Request):
    """
    Invoke the planner agent to analyze the current state and generate a plan
    for the most appropriate next actions.

    Parameters
    ----------
    state : dict
        The current state of the conversation or task, including:
        - user_input: str - The user's input or query
        - context: dict - Additional context information
        - history: list - Previous conversation history
        - metadata: dict - Any additional metadata

    request : Request
        The FastAPI request object containing additional request information

    Returns
    -------
    dict
        A plan object containing:
        - next_action: str - The recommended next action
        - reason: str - Explanation for the chosen action
        - parameters: dict - Parameters needed for the next action
        - confidence: float - Confidence score of the plan (0-1)

    Raises
    ------
    ValueError
        If the input state is invalid or missing required fields
    RuntimeError
        If the planner fails to generate a valid plan

    Examples
    --------
    invoke_planner({
        "user_input": "What's the weather forecast for tomorrow?",
        "context": {"location": "New York"},
        "history": [],
        "metadata": {}
    })
    {
        "next_action": "weather_lookup",
        "reason": "User requested weather information",
        "parameters": {"location": "New York", "date": "tomorrow"},
        "confidence": 0.95
    }
    """
    pass

@agent_router.post("/supervisor")
async def invoke_supervisor(state: dict, request: Request):
    """
        Invoke the supervisor agent to monitor and control the execution of tasks
        and ensure proper coordination between different agents.

        Parameters
        ----------
        state : dict
            The current state of the task execution, including:
            - current_task: str - The task being executed
            - progress: float - Current progress (0-1)
            - results: dict - Partial or complete results
            - errors: list - Any encountered errors
            - context: dict - Additional context information
            - history: list - Previous execution history

        request : Request
            The FastAPI request object containing additional request information

        Returns
        -------
        dict
            A supervision object containing:
            - status: str - Current status (running, completed, failed)
            - next_step: str - Recommended next step
            - control_action: str - Control action to take (continue, pause, stop)
            - metrics: dict - Execution metrics
            - recommendations: list - Recommendations for improvement

        Raises
        ------
        ValueError
            If the input state is invalid or missing required fields
        RuntimeError
            If the supervisor cannot make a valid decision
        TimeoutError
            If the task execution takes too long

        Examples
        --------
        invoke_supervisor({
            "current_task": "document_analysis",
            "progress": 0.75,
            "results": {"pages_processed": 15},
            "errors": [],
            "context": {"document_id": "doc123"},
            "history": [{"step": "load_document", "timestamp": "2025-06-15T14:00:00"}]
        })
        {
            "status": "running",
            "next_step": "extract_key_information",
            "control_action": "continue",
            "metrics": {"processing_rate": 0.5, "error_rate": 0.0},
            "recommendations": ["Consider parallel processing for remaining pages"]
        }
    """
    pass

