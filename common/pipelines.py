# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

from . import schemas, api


def start_pipeline(
    target: schemas.Target,
    profile: str,
) -> schemas.Pipeline:
    return api.make_request(
        "POST",
        "/v1/api/piplines",
        model=schemas.Pipeline,
        payload=schemas.PipelineRequest(target=target, profileName=profile),
    )


def stop_pipeline(exec_id: str):
    api.make_request(
        "DELETE",
        "/v1/api/piplines/" + exec_id,
        model=type(None),
    )
