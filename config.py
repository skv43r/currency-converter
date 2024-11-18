# Этот файл содержит настройки приложения, включая переменные окружения.
# Использует библиотеку pydantic для валидации и управления настройками.

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
