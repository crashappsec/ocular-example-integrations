import os
from typing import Any, Optional, Type, TypeVar

import requests

from . import schemas, constants

_CONTEXT_HEADER = "X-ClusterContext-Name"

Resp = TypeVar("Resp")

class RequestError(BaseException):
    pass

class APIError(BaseException):
    pass

def make_request(
    method: str,
    path: str,
    model: Type[Resp],
    base_url: Optional[str] = None,
    payload: Optional[Any] = None,
    token: Optional[str] = None,
    context_name: Optional[str] = None,
) -> Resp:
    if base_url is None:
        base_url = os.getenv(constants.API_BASE_URL_ENVVAR, "http://aspm-api-server.aspm")
    if context_name is None:
        context_name = os.getenv(constants.CONTEXT_NAME_ENVVAR)

    if token is None:
        try:
            with open(constants.SERVICETOKEN_PATH_ENVVAR, "r", encoding="utf-8") as token_file:
                token = token_file.read()
        except OSError as e:
            raise RequestError("unable to read token: {e}") from e 

    try:
        resp = requests.request(
            method,
            base_url + "/" + path,
            data=payload,
            headers={
                _CONTEXT_HEADER: context_name,
                "Authorization": "Bearer " + token,
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            timeout=60,
        )
    except requests.exceptions.RequestException as e:
        raise RequestError(f"unable to perform request: {e}") from e

    try:
        resp_body = resp.json()
    except requests.JSONDecodeError as e:
        raise RequestError(f"unable to decode json: {e}") from e
    if resp.status_code != 200:
        err = schemas.ErrorResponse.model_validate(resp_body)
        raise APIError(
            f"error from ASPM API (status code {resp.status_code}): {err.message}"
        )
    success_resp = schemas.SuccessResponse[model].model_validate(resp_body)
    return success_resp.response
