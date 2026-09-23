#This file defines all configuration values the app needs
#(DB connection info, app name etc.)
#pydantic settings: automatically reads environment variable sand validate their types.

from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    #MongoDB connection settings
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB_NAME: str = "it_servicedesk"
    # Gives the app a name.
    APP_NAME: str = "IT Service Desk APP API"
    # informs pydantic-settings to load values from .env file 
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
# Shared settings object that all other files can import.
settings = Settings()
    
