from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def home_page():
    return {'message': 'Welcome to fastapi'}
