# Copyright (C) 2025 Crash Override, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the FSF, either version 3 of the License, or (at your option) any later version.
# See the LICENSE file in the root of this repository for full license text or
# visit: <https://www.gnu.org/licenses/gpl-3.0.html>.

FROM python:3.13-slim AS python-uv-slim

WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:0.7 /uv /uvx /bin/

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