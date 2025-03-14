from fastapi import FastAPI
from app.routers import router
from app.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Добро пожаловать на склад рулонов металла!"}
