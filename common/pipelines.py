# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

from typing import Optional

from kubernetes import client

from . import schemas, constants, config


def start_pipeline(
    target: schemas.Target,
    name_prefix: str,
    profile: str,
    downloader: str,
    ttl_seconds: Optional[int] = None,
) -> str:
    api = client.CustomObjectsApi()
    ns = config.get_current_namespace()
    body = {
        "apiVersion": f"{constants.CRD_GROUP}/{constants.CRD_VERSION}",
        "kind": "Pipeline",
        "metadata": {
            "generateName": name_prefix,
        },
        "spec": {
            "downloaderRef": {"name": downloader},
            "profileRef": {"name": profile},
            "target": target.model_dump(),
        },
    }

    if ttl_seconds is not None:
        body["spec"]["ttlSecondsAfterFinished"] = ttl_seconds

    resp = api.create_namespaced_custom_object(
        group=constants.CRD_GROUP,
        version=constants.CRD_VERSION,
        plural=constants.CRD_PIPELINES_PLURAL,
        namespace=ns,
        body=body,
    )
    return resp["metadata"]["name"]


def stop_pipeline(name: str):
    api = client.CustomObjectsApi()
    ns = config.get_current_namespace()
    api.delete_namespaced_custom_object(
        group=constants.CRD_GROUP,
        version=constants.CRD_VERSION,
        plural=constants.CRD_PIPELINES_PLURAL,
        namespace=ns,
        name=name,
    )
