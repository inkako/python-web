from app.config.app import AppSettings
from app.config.database import DatabaseSettings
from app.config.logging import LoggingSettings


class Settings:
    app: AppSettings
    log: LoggingSettings
    db: DatabaseSettings

    def __init__(self):
        self.app = AppSettings()
        self.log = LoggingSettings()
        self.db = DatabaseSettings()