FROM alpine:latest

RUN apk update && \
    apk add --no-cache \
        python3 \
        py3-pip \
        curl 

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN . /venv/bin/activate && \
	pip3 install poetry && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache-dir --upgrade pip setuptools && \
    rm -r /root/.cache

RUN python3 --version && \
    pip3 --version && \
    poetry --version
