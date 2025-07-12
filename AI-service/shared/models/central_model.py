import json
import os
import uuid
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, Union, cast

import pydantic
from pydantic import BaseModel, field
from .base_model import BaseRquest, BaseResponse

class ServerInfo(BaseRquest):
    """Server registration information"""

    name: str
    endpoint: str
    entrypoint: str = ""
    type: Literal["single agent", "multi agent", "orchestrator"]

class TastRequest(BaseRquest): ...

class TaskResponse(BaseResponse):
    task_id: str = Filed(
        deault_factory=lambda: str(uuid.uuid4()),
        description="Unique indentifier for the task",
    )