# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

# This program is an 'Downloader' example.
# Downloaders are given a target identifier and target version
# via the enviornment variables 'ASPM_TARGET_IDENTIFIER' and 'ASPM_TARGET_VERSION'
# and are expected to download the target to the filesystem with the root
# at the working directory. The working directory is referred to as the
# 'target directory' and will also be the scanners working directory.
# This path is also set the environment variable 'ASPM_TARGET_DIR'

# Downloaders are first defined via the api endpoint /api/v1/downloaders/{name}
# where {name} is the identifier for the downloader.

# When starting a pipeline to run on a target, the user provides
# the name of the downloader to use.

import logging
import sys
from argparse import ArgumentParser, Namespace

from common import metadata

logger = logging.getLogger(__name__ + "_downloader")
handler = logging.StreamHandler(sys.stderr)
logger.addHandler(handler)


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--debug", help="enable debug logs", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()

    logger.setLevel(logging.DEBUG if args.debug else logging.INFO)
    ## Pipeline Metadata ##

    # Target to downloader
    target = metadata.get_target_from_env()
    # Its up to the downloader as to what the idenitier
    # And version are used for.
    target_id, target_version = target.identifier, target.version

    # NOTE: the version of a target is optionally, it is up
    # to the downloader to decide what the empty case should mean
    if target_version is None or target_version == "":
        # Handle the empty case here
        target_version = "latest"

    # The name of the downloader is also provided,
    # incase you have multiple downloaders using the same script or container
    downloader = target.downloader

    # Get ID of the pipeline (if needed)
    pipeline_id = metadata.get_pipeline_id_from_env()

    # Optionall get profile name
    profile_name = metadata.get_profile_name_from_env()

    target_dir = metadata.get_target_dir_from_env()

    logger.info(
        "ID %s : profile %s : downloader %s : downloading target '%s' (%s) to %s",
        pipeline_id,
        profile_name,
        downloader,
        target_id,
        target_version,
        target_dir,
    )

    ####################
    ## YOUR CODE HERE ##
    ####################

    # The code should download the target
    # to the directory 'target_dir'. This is also
    # the current working directory of the program

    # Libraries can be added to `pyproject.toml`
    # if needed. The program should exit with non-zero
    # code in case of any errors.

    # If secrets are needed, they can be
    # set in the downloader definition.

    logger.info(
        "ID %s : profile %s : downloader %s: download of target '%s' (%s) to %s is complete",
        pipeline_id,
        profile_name,
        downloader,
        target_id,
        target_version,
        target_dir,
    )


if __name__ == "__main__":
    main()
