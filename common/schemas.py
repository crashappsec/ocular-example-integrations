# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

from enum import Enum
from typing import Generic, Literal, Optional, TypeVar

from pydantic import BaseModel, Field


class Target(BaseModel):
    downloader: str
    identifier: str
    version: Optional[str]


class Status(str, Enum):
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    RUNNING = "Running"
    SUCCESS = "Success"
    FAILURE = "Failure"
    CANCELLED = "Cancelled"
    ERROR = "Error"


class PipelineRequest(BaseModel):
    profile_name: str = Field(alias="profileName")
    target: Target


class Pipeline(BaseModel):
    execution_id: str = Field(alias="id")
    profile: str
    target: Target
    status: Status = Status.UNKNOWN


class SearchRequest(BaseModel):
    crawler_name: str = Field(alias="crawlerName")
    parameters: dict[str, str]


class ScheduledSearchRequest(BaseModel):
    crawler_name: str = Field(alias="crawlerName")
    parameters: dict[str, str]
    schedule: str


class Search(BaseModel):
    execution_id: str = Field(alias="id")
    crawler_name: str = Field(alias="crawlerName")
    parameters: dict[str, str]


class ScheduledSearch(BaseModel):
    execution_id: str = Field(alias="id")
    crawler_name: str = Field(alias="crawlerName")
    parameters: dict[str, str]
    schedule: str


RespT = TypeVar("RespT")


class SuccessResponse(BaseModel, Generic[RespT]):
    success: Literal[True]
    response: RespT


class ErrorResponse(BaseModel, Generic[RespT]):
    success: Literal[False]
    message: str
    # response: Optional[str]
