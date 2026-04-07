from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Carrot Plant API"
    DATABASE_URL: str = "mysql+aiomysql://user:password@localhost:3306/carrot"
    OPENAI_API_KEY: str = ""  # 환경변수 또는 .env 파일에서 로드

    class Config:
        env_file = ".env"


settings = Settings()
