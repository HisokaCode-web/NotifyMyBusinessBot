# NotifyMyBusinessBot 📅

Масштабируемая SaaS-система для записи клиентов через Telegram.

## 🎯 Основные возможности

- ✅ Multi-tenant архитектура (один бот для всех бизнесов)
- ✅ Активация по ключу активации
- ✅ Выбор из 10+ предзаполненных шаблонов ниш
- ✅ Онлайн-запись клиентов
- ✅ Управление расписанием
- ✅ Система уведомлений
- ✅ Админ-панель внутри Telegram
- ✅ Управление сотрудниками
- ✅ Система ролей (Super Admin, Business Owner, Staff, Client)

## 🏗️ Стек технологий

- **Python 3.10+**
- **aiogram 3.x** - Telegram Bot Framework
- **SQLAlchemy 2.0** - ORM
- **SQLite** (разработка) / **PostgreSQL** (production)
- **Alembic** - миграции БД
- **Pydantic** - валидация данных

## 📁 Структура проекта

```
NotifyMyBusinessBot/
├── app/
│   ├── __init__.py
│   ├── main.py                      # Точка входа
│   ├── config.py                    # Конфигурация
│   ├── core/
│   │   ├── __init__.py
│   │   ├── database.py              # SQLAlchemy setup
│   │   ├── security.py              # Шифрование
│   │   └── constants.py             # Константы и нишы
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py                  # Базовая модель
│   │   ├── user.py                  # Пользователи
│   │   ├── business.py              # Бизнесы
│   │   ├── service.py               # Услуги
│   │   ├── booking.py               # Записи
│   │   ├── schedule.py              # Расписание
│   │   └── invitation_key.py         # Ключи активации
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   ├── business_service.py
│   │   ├── booking_service.py
│   │   ├── niche_service.py
│   │   └── notification_service.py
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── start.py
│   │   ├── activation.py
│   │   ├── business_setup.py
│   │   ├── booking_client.py
│   │   ├── admin_panel.py
│   │   ├── super_admin.py
│   │   └── common.py
│   ├── states/
│   │   ├── __init__.py
│   │   ├── activation.py
│   │   ├── business_setup.py
│   │   ├── booking.py
│   │   └── admin.py
│   ├── keyboards/
│   │   ├── __init__.py
│   │   ├── activation.py
│   │   ├── business.py
│   │   ├── booking.py
│   │   └── admin.py
│   ├── filters/
│   │   ├── __init__.py
│   │   ├── role_filter.py
│   │   └── business_filter.py
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── context_middleware.py
│   │   ├── auth_middleware.py
│   │   └── logger_middleware.py
│   └── utils/
│       ├── __init__.py
│       ├── validators.py
│       ├── formatters.py
│       └── helpers.py
├── migrations/                      # Alembic миграции
├── tests/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Быстрый старт

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/HisokaCode-web/NotifyMyBusinessBot.git
cd NotifyMyBusinessBot
```

### 2. Установите зависимости

```bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Создайте .env файл

```bash
cp .env.example .env
```

Отредактируйте `.env` и добавьте:
- `TELEGRAM_BOT_TOKEN` - токен вашего бота
- `TELEGRAM_BOT_USERNAME` - юзернейм бота
- `SUPER_ADMIN_IDS` - ваш Telegram ID

### 4. Запустите бота

```bash
python -m app.main
```

## 📚 Документация

### Для разработчиков
- [Архитектура](docs/ARCHITECTURE.md)
- [FSM состояния](docs/FSM.md)
- [API сервисов](docs/SERVICES.md)
- [Модели БД](docs/DATABASE.md)

### Для пользователей
- [Инструкция владельца бизнеса](docs/OWNER_GUIDE.md)
- [Инструкция клиента](docs/CLIENT_GUIDE.md)

## 💡 Основные концепции

### Multi-tenant архитектура

Один бот обслуживает неограниченное количество бизнесов.
Каждый бизнес имеет:
- Свои услуги
- Своё расписание
- Своих клиентов
- Свои настройки

```
🤖 Один Telegram Bot
    ├── 📍 Business #1 (Barbershop)
    │   ├── 💇 Services: стрижка, покраска...
    │   └── 👥 Clients: Иван, Мария...
    ├── 📍 Business #2 (Dentistry)
    │   ├── 🦷 Services: чистка, пломба...
    │   └── 👥 Clients: Петр, Анна...
    └── 📍 Business #3 (Gym)
        ├── 🏋️ Services: тренировка, йога...
        └── 👥 Clients: Александр, Ольга...
```

### Система ролей

- **Super Admin** - разработчик (создание ключей, статистика)
- **Business Owner** - владелец бизнеса (управление услугами, персоналом)
- **Business Staff** - сотрудник бизнеса (просмотр расписания)
- **Client** - клиент (запись на услугу)

## 🔐 Безопасность

- Ключи активации хешируются (SHA-256)
- Пароли шифруются (Fernet)
- Права доступа проверяются на каждый запрос
- SQL injection защита (SQLAlchemy ORM)

## 📊 Бизнес-модель

### SaaS монетизация

1. **Freemium**
   - Бесплатно до 10 записей/месяц
   - Потом $9.99/месяц

2. **Подписка по уровням**
   - Starter: $9.99 (50 записей)
   - Professional: $29.99 (500 записей)
   - Enterprise: custom (неограниченно)

3. **White-label**
   - Собственный бот на вашем аккаунте
   - Интеграция с вашим сайтом

## 🤝 Вклад

Если хотите помочь проекту:

1. Fork репозиторий
2. Создайте ветку (`git checkout -b feature/AmazingFeature`)
3. Закоммитьте изменения (`git commit -m 'Add some AmazingFeature'`)
4. Push в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📄 Лицензия

MIT License - смотрите [LICENSE](LICENSE)

## 👨‍💼 Автор

**HisokaCode-web** - Senior Python Developer

## 📞 Контакты

- Telegram: @HisokaCode
- GitHub: [@HisokaCode-web](https://github.com/HisokaCode-web)

---

**Made with ❤️ for business automation**