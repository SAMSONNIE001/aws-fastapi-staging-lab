import os
from fastapi import FastAPI

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "development")

@app.get("/")
def home():
    return {"message": "Elastic Beanstalk CI/CD deployment is working"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "environment": APP_ENV
    }
