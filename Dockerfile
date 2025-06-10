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