FROM python:3.6

RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install pipenv

WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
COPY temp.txt .
RUN pipenv sync
ADD tests/ tests/

ENTRYPOINT ["pipenv", "run"]