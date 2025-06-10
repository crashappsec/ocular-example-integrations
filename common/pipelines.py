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
