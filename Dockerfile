FROM python:3.10
VOLUME /help_you
COPY . .
WORKDIR .
RUN pip install poetry
RUN potery install
