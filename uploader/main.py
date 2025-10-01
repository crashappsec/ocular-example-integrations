# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

# This program is an 'Uploader' example.
# Uploaders are given a list of file paths via the CLI args
# (after the argument '--') and are expected to upload or
# process the results to be sent to 3rd party services

# Uploaders are first defined via the api endpoint /api/v1/uploaders/{name}
# where {name} is the identifier for the uploader.

# In a 'Profile' you can then specify which uploader
# to run when the scans are complete
# (and what files are expected to be uploaded)

import logging
import sys
from argparse import REMAINDER, ArgumentParser, Namespace

from common import metadata, parameters

logger = logging.getLogger(__name__ + "_uploader")
handler = logging.StreamHandler(sys.stderr)
logger.addHandler(handler)


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--debug", help="enable debug logs", action="store_true")
    parser.add_argument("artifacts", nargs=REMAINDER, help="Artifacts to upload")
    return parser.parse_args()


def main():
    args = parse_args()
    logger.setLevel(logging.DEBUG if args.debug else logging.INFO)

    # Parse artifacts from CLI
    artifacts = []
    for idx, arg in enumerate(args.artifacts):
        if arg == "--":
            artifacts = args.artifacts[idx + 1 :]

    ## Parameters ##
    # If a parameter is needed, use 'parameters.get_value'
    # Will be 'NONE' if not set. Parameters can be set via
    # the definition, see the file `definition.yaml` in this directory
    my_param = parameters.get_value("MY_PARAM")
    if my_param is None:
        my_param = "default_value"

    ## Pipeline Metadata ##

    # Target that the pipeline was run on
    target_id = metadata.get_target_identifier_from_env()

    # ID of the pipeline
    pipeline_name = metadata.get_pipeline_name_from_env()

    # get_profile_name_from_env
    profile_name = metadata.get_profile_name_from_env()

    # Name uploader provided by user, this is useful if the same container image
    # is used by multiple uploader
    uploader_name = metadata.get_uploader_name_from_env()

    logger.info(
        "pipeline %s : uploader %s : profile %s : uploading artifacts %s from target %s",
        pipeline_name,
        uploader_name,
        profile_name,
        artifacts,
        target_id,
    )

    for artifact in artifacts:
        logger.debug(
            "pipeline %s : profile %s : uploading artfact %s",
            pipeline_name,
            profile_name,
            artifact,
        )

        ####################
        ## YOUR CODE HERE ##
        ####################

        # The code should upload each file in
        # the list to where you want.

        # Libraries can be added to `pyproject.toml`
        # if needed. The program should exit with non-zero
        # code in case of any errors.

        # If secrets or parameters are needed, they can be
        # set in the uploader definition.

    logger.info(
        "pipeline %s : profile %s : upload complete", pipeline_name, profile_name
    )


if __name__ == "__main__":
    main()
