FROM python:3.12.2-windowsservercore-ltsc2022

RUN pip install --no-cache-dir --upgrade pip \
    pip install poetry teamcity-messages

ENTRYPOINT ["cmd"]
