from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Carrot Plant API"
    DATABASE_URL: str = "mysql+aiomysql://user:password@localhost:3306/carrot"

    class Config:
        env_file = ".env"


settings = Settings()
