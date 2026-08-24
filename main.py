import os
import json
import boto3
from botocore.exceptions import ClientError
from fastapi import FastAPI

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "development")
AWS_REGION = os.getenv("AWS_REGION", "eu-west-2")
SECRET_NAME = os.getenv(
    "SECRET_NAME",
    "fastapi/staging/demo-api-key"
)


def get_demo_api_key():
    try:
        client = boto3.client(
            "secretsmanager",
            region_name=AWS_REGION
        )

        response = client.get_secret_value(
            SecretId=SECRET_NAME
        )

        secret = json.loads(response["SecretString"])

        return secret.get("DEMO_API_KEY")

    except (ClientError, KeyError, json.JSONDecodeError):
        return None


DEMO_API_KEY = get_demo_api_key()


@app.get("/")
def home():
    return {
        "message": "Elastic Beanstalk CI/CD deployment is working"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "environment": APP_ENV,
        "secret_loaded": DEMO_API_KEY is not None
    }
