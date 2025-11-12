from fastapi import FastAPI
from .api.routes import router as api_router

__all__ = ["app", "read_root"]
