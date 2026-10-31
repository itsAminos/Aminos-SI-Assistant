from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    bot_token: str
    llm_api_key: str

    model_config = SettingsConfigDict(env_file=".env",  env_file_endoding="utf-8")

config = Settings()