from fastapi import FastAPI

from app.routers import router


app = FastAPI()

app.include_router(router)


@app.get("/")
def read_root():
    """Проверка связи"""
    return {"message": "Добро пожаловать на склад рулонов металла!"}
