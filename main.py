# Главный файл приложения, который инициализирует FastAPI и включает маршруты.
# Запускает приложение, используя Uvicorn в качестве ASGI сервера.

from fastapi import FastAPI
from routes import router as main_router

app = FastAPI(title="Currency Converter API")
app.include_router(main_router)
