"""Конфигурация приложения.

Все переменные читаются из .env файла.
Используется Pydantic v2 для валидации.
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Конфигурация приложения."""
    
    # Telegram
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_BOT_USERNAME: str
    
    # Database
    DATABASE_URL: str = "sqlite:///./booking_bot.db"
    DATABASE_ECHO: bool = False  # логирование SQL запросов
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    
    # Business logic
    ACTIVATION_KEY_LENGTH: int = 8
    BOOKING_REMINDER_HOURS: int = 24
    MAX_SERVICES_PER_BUSINESS: int = 50
    MAX_BOOKINGS_PER_DAY: int = 200
    
    # Features
    ENABLE_NOTIFICATIONS: bool = True
    ENABLE_REMINDERS: bool = True
    WEBHOOK_URL: Optional[str] = None
    POLLING_MODE: bool = True
    
    # Timezone
    DEFAULT_TIMEZONE: str = "Europe/Moscow"
    
    # Admin
    SUPER_ADMIN_IDS: list[int] = [123456789]  # Ваш Telegram ID
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Создаём глобальный инстанс
settings = Settings()
