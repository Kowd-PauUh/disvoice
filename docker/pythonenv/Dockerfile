FROM python:3.10-slim-buster

ARG PROJECT_DIR

COPY docker/pythonenv/entrypoint.sh /
COPY docker/pythonenv/requirements.txt /

COPY audios/ ${PROJECT_DIR}/audios/
COPY disvoice/ ${PROJECT_DIR}/disvoice/
COPY docs/ ${PROJECT_DIR}/docs/
COPY images/ ${PROJECT_DIR}/images/
COPY notebooks_examples/ ${PROJECT_DIR}/notebooks_examples/
COPY tests/ ${PROJECT_DIR}/tests/

COPY install.sh/ ${PROJECT_DIR}/install.sh
COPY requirements.txt/ ${PROJECT_DIR}/requirements.txt
COPY setup.cfg/ ${PROJECT_DIR}/setup.cfg
COPY setup.py/ ${PROJECT_DIR}/setup.py

ENV PYTHONPATH=${PROJECT_DIR}

RUN printf '#!/bin/sh\nexit 0\n' > /usr/sbin/policy-rc.d \
 && apt-get update -yqq \
 && apt-get install -y --no-install-recommends curl tar build-essential praat \
 && apt-get autoremove -yqq --purge \
 && apt-get clean \
 && chmod +x /entrypoint.sh \
 && pip install --no-cache-dir -U -r /requirements.txt

WORKDIR ${PROJECT_DIR}

ENTRYPOINT ["/entrypoint.sh"]
