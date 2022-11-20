FROM python:3.10

RUN apt-get update && apt-get install -y espeak
RUN mkdir app
COPY . app/

WORKDIR /app
RUN pip install .

ENTRYPOINT [ "python", "main.py" ]
