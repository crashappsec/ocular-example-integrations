import os
from typing import Optional


def get_value(name: str) -> Optional[str]:
    """Returns the value for the given parameter name, or None if not set"""
    env_name = "OCULAR_PARAM_" + name.replace("-", "_").upper()
    return os.getenv(env_name)
