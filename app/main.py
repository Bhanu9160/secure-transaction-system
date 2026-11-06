from fastapi import FastAPI
from app.database import engine, Base

import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure Transaction Management System",
    description="A simulated secure money transaction platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Secure Transaction Management System",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}