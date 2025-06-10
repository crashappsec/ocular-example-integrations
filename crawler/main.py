# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

# This program is an 'Crawler' example.
# Crawler are expected to enumerate targets to scan and trigger pipelines
# for each. It will have an authetnicated token made available to it.

# Crawler are first defined via the api endpoint /api/v1/crawlers/{name}
# where {name} is the identifier for the downloader.

# Crawlers are either invoked ad-hoc, or set on a schedule to run.

import logging
import sys
from argparse import ArgumentParser, Namespace
from typing import List

from common import metadata, parameters, pipelines, schemas, api

logger = logging.getLogger(__name__ + "_crawler")
handler = logging.StreamHandler(sys.stderr)
logger.addHandler(handler)


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--debug", help="enable debug logs", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    logger.setLevel(logging.DEBUG if args.debug else logging.INFO)

    ## Crawler Metadata ##

    # Read crawler name from env.
    # This can be used when the same container image
    # is ran for different crawlers
    crawler_name = metadata.get_crawler_name_from_env()

    ## Parameters ##

    # If a parameter is needed, use 'parameters.get_value'
    # Will be 'NONE' if not set
    ## NOTE: these params are just examples, you will need to
    ## configure parameters in the definition if desired.
    profile = parameters.get_value("PROFILE_NAME")
    if profile is None:
        profile = "default"

    logger.info("Crawler %s : beginning target enumeration", crawler_name)

    targets: List[schemas.Target] = []

    # targets.append(schemas.Target{
    #     identifier="https://my.git.org/repo",
    #     downloader="git",
    #     version="my-cool-branch"
    # })

    ####################
    ## YOUR CODE HERE ##
    ####################

    # The code should enumerate targets
    # and append them to the 'targets' array.
    # Each elemnet should be a schema.

    # Libraries can be added to `pyproject.toml`
    # if needed. The program should exit with non-zero
    # code in case of any errors.

    # If secrets or parameters are needed, they can be
    # set in the downloader definition.

    for t in targets:
        logger.info(
            "Crawler %s : profile %s : downloader %s : starting pipeline for target %s (%s)",
            crawler_name,
            profile,
            t.downloader,
            t.identifier,
            t.version,
        )
        try:
            pline = pipelines.start_pipeline(t, profile)
            logger.debug(
                "Crawler %s : profile %s : downloader %s : pipeline started %s (%s) - ID: %s",
                crawler_name,
                profile,
                t.downloader,
                t.identifier,
                t.version,
                pline.execution_id,
            )
        except (api.RequestError, api.APIError) as e:
            logger.error(
                "Crawler %s : profile %s : downloader %s : "
                "unable to start pipeline for target %s (%s) - %s",
                crawler_name,
                profile,
                t.downloader,
                t.identifier,
                t.version,
                e,
            )
    logger.info("Crawler %s: crawl complete", crawler_name)


if __name__ == "__main__":
    main()
