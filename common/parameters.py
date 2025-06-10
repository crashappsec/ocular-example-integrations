# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

import os
from typing import Optional


def get_value(name: str) -> Optional[str]:
    """Returns the value for the given parameter name, or None if not set"""
    env_name = "OCULAR_PARAM_" + name.replace("-", "_").upper()
    return os.getenv(env_name)
