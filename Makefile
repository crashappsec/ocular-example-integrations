# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

OCULAR_ENV_FILE ?= .env

# Only if .env file is present
ifneq (,$(wildcard ${OCULAR_ENV_FILE}))
	include ${OCULAR_ENV_FILE}
endif

# logging level debug when using make
OCULAR_LOGGING_LEVEL ?= debug

DOCKER_BUILDKIT ?= 1

ifneq ($(DOCKER_DEFAULT_PLATFORM),)
	export DOCKER_DEFAULT_PLATFORM
endif

OCULAR_CRAWLER_IMG ?= ocular-example-crawler:latest
OCULAR_DOWNLOADER_IMG ?= ocular-example-downloader:latest
OCULAR_UPLOADER_IMG ?= ocular-example-uploader:latest

export

.PHONY: all
all: docker-build-all

#########
# Build #
#########


################
# Docker Build #
################

.PHONY: docker-build-all
docker-build-all: docker-build-crawler docker-build-uploader docker-build-downloader

.PHONY: docker-build-crawler
docker-build-crawler:
	@docker build -t ${OCULAR_CRAWLER_IMG} --build-arg PROGRAM=crawler .

.PHONY: docker-build-downloader
docker-build-downloader:
	@docker build -t ${OCULAR_DOWNLOADER_IMG} --build-arg PROGRAM=downloader .

.PHONY: docker-build-uploader
docker-build-uploader:
	@docker build -t ${OCULAR_UPLOADER_IMG} --build-arg PROGRAM=uploader .


##############
# Publishing #
##############

.PHONY: docker-push-all
docker-push-all: docker-push-crawler docker-push-downloader docker-push-uploader

.PHONY: docker-push-crawler
docker-push-crawler:
	@docker push ${OCULAR_CRAWLER_IMG}

.PHONY: docker-push-downloader
docker-push-downloader:
	@docker push ${OCULAR_DOWNLOADER_IMG}

.PHONY: docker-push-uploader
docker-push-uploader:
	@docker push ${OCULAR_UPLOADER_IMG}


###############
# Development #
###############

.PHONY: lint fmt test fmt-code fmt-license

lint:
	@echo "Running linters ..."
	@uv run pylint .
	@uv run black --check .

fmt: fmt-code fmt-license

fmt-license:
	@echo "Formatting license headers ..."
	@license-eye header fix

fmt-code:
	@echo "Running code formatters ..."
	@uv run black .

test:
	@echo "Running unit tests ..."
	@echo "TODO"
