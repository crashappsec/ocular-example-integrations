GO_SOURCES=$(shell find . -name '*.go' -not -path './cmd/*')

OCULAR_ENV_FILE ?= .env

# Only if .env file is present
ifneq (,$(wildcard ${OCULAR_ENV_FILE}))
	include ${OCULAR_ENV_FILE}
endif

OCULAR_ENVIRONMENT ?= development

# logging level debug when using make
OCULAR_LOGGING_LEVEL ?= debug

DOCKER_BUILDKIT ?= 1

ifneq ($(DOCKER_DEFAULT_PLATFORM),)
	export DOCKER_DEFAULT_PLATFORM
endif
OCULAR_IMAGE_REGISTRY ?= ghcr.io
OCULAR_IMAGE_TAG ?= local

OCULAR_EXAMPLE_CRAWLER_IMAGE_REPOSITORY ?= crashappsec/ocular-example-crawler
OCULAR_EXAMPLE_DOWNLOADER_IMAGE_REPOSITORY ?= crashappsec/ocular-example-downloader
OCULAR_EXAMPLE_UPLOADER_IMAGE_REPOSITORY ?= crashappsec/ocular-example-uploader

OCULAR_EXAMPLE_DOWNLOADER_IMAGE ?= ${OCULAR_IMAGE_REGISTRY}/${OCULAR_EXAMPLE_DOWNLOADER_IMAGE_REPOSITORY}:${OCULAR_IMAGE_TAG}
OCULAR_EXAMPLE_CRAWLER_IMAGE ?= ${OCULAR_IMAGE_REGISTRY}/${OCULAR_EXAMPLE_CRAWLER_IMAGE_REPOSITORY}:${OCULAR_IMAGE_TAG}
OCULAR_EXAMPLE_UPLOADER_IMAGE ?= ${OCULAR_IMAGE_REGISTRY}/${OCULAR_EXAMPLE_UPLOADER_IMAGE_REPOSITORY}:${OCULAR_IMAGE_TAG}

export

.PHONY: all
all: build-docker

#########
# Build #
#########


################
# Docker Build #
################

.PHONY: build-docker build-docker-example-crawler build-docker-example-downloader build-docker-example-uploader
build-docker:
	@docker compose build

build-docker-example-crawler:
	@docker compose build crawler

build-docker-example-downloader:
	@docker compose build downloader

build-docker-example-uploader:
	@docker compose build uploader


##############
# Publishing #
##############

.PHONY: push-docker
push-docker: build-docker
	@docker compose push

###############
# Development #
###############

.PHONY: lint fmt test fmt-code fmt-license

lint:
	@echo "Running linters ..."
	@uv run pylint .
	@uv run black --check 

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
