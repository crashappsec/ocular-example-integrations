# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

#################
# K8s Resources #
#################

# Define the custom resource details from your CRD.
CRD_GROUP = "ocular.crashoverride.run"
CRD_VERSION = "v1beta1"
CRD_PIPELINES_PLURAL = "pipelines"

###########################
## Environment Variables ##
###########################

TARGET_IDENTIFIER_ENVVAR = "OCULAR_TARGET_IDENTIFIER"
TARGET_VERSION_ENVVAR = "OCULAR_TARGET_VERSION"
DOWNLOADER_NAME_ENVVAR = "OCULAR_DOWNLOADER_NAME"

PROFILE_NAME_ENVVAR = "OCULAR_PROFILE_NAME"
PIPELINE_NAME_ENVVAR = "OCULAR_PIPELINE_NAME"
SEARCH_NAME_ENVVAR = "OCULAR_SEARCH_NAME"

RESULTS_DIR_ENVVAR = "OCULAR_RESULTS_DIR"
TARGET_DIR_ENVVAR = "OCULAR_TARGET_DIR"

CRAWLER_NAME_ENVVAR = "OCULAR_CRAWLER_NAME"

UPLOADER_NAME_ENVVAR = "OCULAR_UPLOADER_NAME"
