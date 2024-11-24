# Stage 1: Build Stage
FROM python:3.12.7-bookworm AS build

ARG ENVIRONMENT
ENV PYTHONUNBUFFERED=1

RUN pip install uv

WORKDIR /code
COPY requirements.lock requirements-dev.lock ./

ENV UV_HTTP_TIMEOUT=300
ENV UV_INSTALL_DIR=/root/.local/bin

RUN uv pip install --no-cache --system -r requirements.lock

WORKDIR /code
COPY . /code/