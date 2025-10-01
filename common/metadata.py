# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

import os

from . import constants


def get_target_identifier_from_env() -> str:
    """Reads the target identifier for the pipeline
    from the enviornment."""

    return os.getenv(constants.TARGET_IDENTIFIER_ENVVAR, "unknown")


def get_target_version_from_env() -> str:
    """Reads the target version for the pipeline
    from the enviornment."""

    return os.getenv(constants.TARGET_VERSION_ENVVAR, "unknown")


def get_downloader_name_from_env() -> str:
    """Reads the downlodaer name for the current pipeline."""

    return os.getenv(constants.DOWNLOADER_NAME_ENVVAR, "unknown")


def get_pipeline_name_from_env() -> str:
    """Reads the name of the current pipeline
    from the enviornment."""

    return os.getenv(constants.PIPELINE_NAME_ENVVAR, "unknown")


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


def get_search_name_from_env() -> str:
    return os.getenv(constants.SEARCH_NAME_ENVVAR, "unknown")


def get_results_dir_from_env() -> str:
    """Returns the directory for uploading artifacts
    as read from the current enviornment."""

    return os.getenv(constants.RESULTS_DIR_ENVVAR, "/mnt/results")


def get_target_dir_from_env() -> str:
    """Returns the directory for downloading and scanning
    the target as read from the current enviornment."""

    return os.getenv(constants.TARGET_DIR_ENVVAR, "/mnt/target")
