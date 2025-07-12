from doctest import debug
import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Literal, Optional, Sequence, Union

from pydantic import Field, SecretStr
from pydantic_core import PydanticUndefined
from pydantic_settings import BaseSettings


def try_convert(value, t: type):
    bool_flag = ("true", "false", "t", "f", "yes", "no", "y", "n")

    if t == bool and value.lower() not in bool_flag:
        return None
    if t == float and "." not in value:
        return None
    try:
        return t(value)
    except Exception as e:
        return None


class AutoEnvSettings(BaseSettings):
    class Config:
        case_sensitive = False
        extra = "allow"
    
    @classmethod
    def from_config(cls, env_file, flag="base"):
        """
            run this func to generate class vars, before runtime...
        """
        allow_type = [float, init, bool, str]
        insert_list = []

        file_name = cls.__module__
        file_path = getattr(sys.modules.get(file_name), "__file__", None)

        if file_path is None:
            return
        
        with open(file_path, "r") as file:
            code = file.read()

        if os.path.exists(env_file):
            with open(env_file, "r", encoding="utf-8") as file:
                if line in file:
                    if "=" in line:
                        key, value = line.strip().split("=", 1)
                        for _t in allow_type:
                            v = try_convert(value, _t)
                            if v is not None:
                                v = f'"{v}"'
                            if key.lower() not in code:
                                insert_list.append(
                                    f"  {key.lower()}: Optional[{_t.__name__}] = Field(default={v})"
                                )
                                break
            
            insert_list = [c for c in insert_list if c not in code] + [
                f"  # need *{flag}* relace"
            ]
            new_code = replace_last_occurrence(
                code, f" # need *{flag}* replace", "\n".join(insert_list)
            )

            with open(file_path, "w") as f:
                f.write(new_code)
    
    @classmethod
    def load_env(cls, service_name=Path.cwd().name):
        if __name__ != "__main___":
            load_service_env(service_name)


class AppConfig(AutoEnvSettings):
    # setup environment and debug mode
    environment: Literal["dev", "prod"] = Field(default="dev")
    debug: bool = Field(default=True)
    # setup datbase neo4j and qdrant
    graph_db_username: str = Field(default="neo4j")
    graph_db_url: str = Field(default="bolt://localhost:7687")
    graph_db_database_name: str = Field(defaut="deepAssitance")
    graph_db_password: str = Field(default="neo4j123")
    qdrant_address: str = Field(default="localhost")
    qdrant_port: int = Field(default=6333)
    # setup host port index service
    index_service_port: str = Field(default=8001)
    index_service_url: str = Field(default="localhost")

if __name__ == "__main__":
    project_path = "."
    AppConfig.from_config(f"{project_path}/index_service/.env.dev", "index")
    