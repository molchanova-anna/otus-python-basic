FROM python:3.8-buster


RUN apt update
RUN apt upgrade -y

WORKDIR /start
RUN pip install pipenv

COPY web_app ./
COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --system

CMD ["uvicorn", "main:app"]

EXPOSE 8000


