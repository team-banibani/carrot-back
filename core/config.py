from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    APP_NAME: str = "Carrot Plant API"
    DATABASE_URL: str

    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o-mini"
    MAX_IMAGE_SIZE: int = 5242880  # 5MB
    MAX_IMAGES: int = 3


settings = Settings()
