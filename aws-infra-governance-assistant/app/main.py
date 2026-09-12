from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="AWS Infra Governance Assistant",
    version="1.0.0"
)

app.include_router(router)