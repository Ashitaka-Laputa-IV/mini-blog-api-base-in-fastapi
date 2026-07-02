from fastapi import FastAPI

from app.database import Base, engine
from app.routers import posts

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini Blog API")

app.include_router(posts.router)
