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
