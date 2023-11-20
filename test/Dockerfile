FROM python:3.11

WORKDIR /app

COPY *.py requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT python stream_flag_value.py

