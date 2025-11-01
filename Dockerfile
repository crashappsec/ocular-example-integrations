# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

FROM ghcr.io/astral-sh/uv:0.9.7@sha256:ba4857bf2a068e9bc0e64eed8563b065908a4cd6bfb66b531a9c424c8e25e142 AS astral

FROM python:3.14-slim@sha256:4ed33101ee7ec299041cc41dd268dae17031184be94384b1ce7936dc4e5dead3 AS python-uv-slim

WORKDIR /app
COPY --from=astral  /uv /uvx /bin/

FROM python-uv-slim AS builder

COPY . /app
WORKDIR /app

RUN uv sync --locked

RUN uv build --out-dir dist

FROM python-uv-slim AS final

ARG PROGRAM
ENV ENTRYPOINT=${PROGRAM}

RUN useradd --create-home appuser

COPY /${PROGRAM}/ /app/
COPY --from=builder /app/dist/ /tmp/wheels/


RUN uv pip install --no-cache --system /tmp/wheels/*.whl && \
    rm -rf /tmp/wheels/

USER appuser

ENTRYPOINT [ "python3", "main.py", "--debug"]