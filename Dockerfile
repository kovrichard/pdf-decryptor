FROM python:3.10.4-alpine3.16 as base

RUN apk update && apk upgrade
RUN apk add --no-cache qpdf && \
    apk add --no-cache --virtual .build-deps curl gcc musl-dev

RUN curl -sSL https://install.python-poetry.org | python && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

RUN mkdir -p /usr/src/app/
COPY ./ ./usr/src/app/
WORKDIR /usr/src/app/

FROM base AS final

RUN poetry export -f requirements.txt > requirements.txt && \
    pip install -r requirements.txt && apk del .build-deps && rm -rf /root/.poetry /root/.cache

CMD gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 "pdf_decryptor.server.factory:create_app()"

FROM base as test

RUN poetry install && \
    rm -rf /usr/src/app/*

RUN apk --purge del .build-deps
