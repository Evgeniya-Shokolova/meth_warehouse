from fastapi import FastAPI

from app.database import Base, engine
from app.routers import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Добро пожаловать на склад рулонов металла!"}
