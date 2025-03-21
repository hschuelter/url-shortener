from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    frontend_url: str
    alternate_url1: str
    alternate_url2: str

    database_host : str
    database_user : str
    database_password : str
    database_name : str
    database_psql : str

    model_config = SettingsConfigDict(env_file=".env")