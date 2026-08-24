from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Elastic Beanstalk CI/CD deployment is working"}

@app.get("/health")
def health():
    return {"status": "ok", "environment": "staging"}
