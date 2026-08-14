from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    environment: str
    database_path: str

    whatsapp_access_token: str | None = None
    whatsapp_phone_number_id: str | None = None
    whatsapp_verify_token: str
    whatsapp_dry_run: bool = False
    whatsapp_api_version: str = "v25.0"

    google_calendar_id: str = "primary"
    google_credentials_path: str = "credentials/google_credentials.json"
    google_token_path: str = "credentials/google_token.json"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
