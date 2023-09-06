FROM python:3.11.5-alpine3.18

RUN apk add curl

RUN curl -sL https://github.com/openfaas/classic-watchdog/releases/download/0.2.2/fwatchdog-amd64 > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog

ENV fprocess="python entrypoint.py"
COPY entrypoint.py /

EXPOSE 8080
CMD [ "fwatchdog" ]