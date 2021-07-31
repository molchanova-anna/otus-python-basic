from fastapi import FastAPI

my_app = FastAPI()


@my_app.get("/ping")
def default_message():
    return {'message': 'pongg'}
