from fastapi import FastAPI
import requests

app = FastAPI()


@app.post("/searches/organizations")
def make_request(payload: dict):

    return "hello"