# сборка контейнера
# docker build . -t web-app

# запуск контейнера
# docker run -p 8080:8000 web-app

FROM python:3.8-buster


RUN apt update
RUN apt upgrade -y

WORKDIR /start
RUN pip install pipenv

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --system

COPY web_app ./web_app

EXPOSE 8000

CMD ["uvicorn", "web_app.main:my_app"]


