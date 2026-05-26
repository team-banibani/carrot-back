from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Carrot Plant API"
    DATABASE_URL: str = "mysql+aiomysql://user:password@localhost:3306/carrot"
    OPENAI_API_KEY: str = ""  # 환경변수 또는 .env 파일에서 로드

    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o-mini"
    MAX_IMAGE_SIZE: int = 5242880  # 5MB
    MAX_IMAGES: int = 3

    class Config:
        env_file = ".env"


settings = Settings()
