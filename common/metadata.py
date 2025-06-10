import os

from . import constants, schemas


def get_target_from_env() -> schemas.Target:
    """Parses the [schemas.Target] from the enviornment."""
    return schemas.Target(
        downloader=os.getenv(constants.TARGET_DOWNLOADER_ENVVAR, ""),
        identifier=os.getenv(constants.TARGET_IDENTIFIER_ENVVAR, ""),
        version=os.getenv(constants.TARGET_VERSION_ENVVAR),
    )


def get_pipeline_id_from_env() -> str:
    """Reads the ID of the current pipeline
    from the enviornment."""

    return os.getenv(constants.PIPELINE_ID_ENVVAR, "unknown")


def get_profile_name_from_env() -> str:
    """Reads the profile name used to start the pipeline
    from the enviornment."""

    return os.getenv(constants.PROFILE_NAME_ENVVAR, "unknown")


def get_uploader_name_from_env() -> str:
    """returns the name of the current uploader"""

    return os.getenv(constants.UPLOADER_NAME_ENVVAR, "unknown")


def get_crawler_name_from_env() -> str:
    """returns the name of the current crawler"""

    return os.getenv(constants.CRAWLER_NAME_ENVVAR, "unknown")


def get_results_dir_from_env() -> str:
    """Returns the directory for uploading artifacts
    as read from the current enviornment."""

    return os.getenv(constants.RESULTS_DIR_ENVVAR, "/mnt/results")


def get_target_dir_from_env() -> str:
    """Returns the directory for downloading and scanning
    the target as read from the current enviornment."""

    return os.getenv(constants.TARGET_DIR_ENVVAR, "/mnt/target")
