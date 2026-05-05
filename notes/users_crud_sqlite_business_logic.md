# Users CRUD + SQLite Progress

## Что уже реализовано

### Users entity

Создали полноценную сущность пользователей.

### Fields

- id
- first_name
- last_name
- email
- role
- progress
- certificate
- is_active

---

## Pydantic Schema

Файл:
app/schemas/user.py

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    role: str
    progress: int = 0
    certificate: bool = False
    is_active: bool = True

---

## SQLAlchemy Model

Файл:
app/models/user.py

from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, nullable=False)
    progress = Column(Integer, default=0)
    certificate = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

---

## Router подключение

Файл:
app/main.py

Добавили импорт:

from app.routes.users import router as users_router
from app.models.user import User

И подключили router:

app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)

---

## POST /users/

Создание пользователя через SQLite database.

Работает через:

- Depends()
- SessionLocal()
- db.add()
- db.commit()
- db.refresh()

Проверка через Swagger успешна.

Данные сохраняются в:

mini_lms.db

Таблица:

users

---

## GET /users/

Получение всех пользователей из SQLite.

return db.query(UserModel).all()

Работает корректно.

Swagger + DB Browser проверены.

---

## GET /users/{user_id}

Получение конкретного пользователя по id.

Логика:

- поиск пользователя по id
- если найден → вернуть user
- если не найден → вернуть message

Пример:

GET /users/1

---

## PUT /users/{user_id}

Обновление progress пользователя.

Логика:

- поиск пользователя по id
- обновление progress
- бизнес-логика certificate

Пример:

PUT /users/1?progress=100

Результат:

progress = 100 → certificate = True
progress < 100 → certificate = False

Важно:

Сейчас PUT реализован как отдельный endpoint для progress,
а не как full update всей сущности.

---

## PATCH /users/{user_id}

Частичное обновление пользователя.

Можно менять только отдельные поля.

Пример:

{
    "first_name": "Roman Updated"
}

или

{
    "progress": 100
}

PATCH не требует передавать всю модель.

PATCH = partial update.

---

## DELETE /users/{user_id}

Удаление пользователя по id.

Проверено:

- удаление через Swagger
- удаление из SQLite

Работает корректно.

---

## PUT vs PATCH

PUT:

- обычно full update
- у нас сейчас используется для update progress

PATCH:

- partial update
- можно передать только одно поле

Пример:

{
    "first_name": "Ro"
}

---

## SQLite boolean

SQLite отображает boolean как:

- 0 = False
- 1 = True

Это нормальное поведение.

Пример:

certificate = 0 → False
certificate = 1 → True

Исправлять ничего не нужно.

---

## Что дальше

Следующий этап:

API Test Cases

Создаем файл:

notes/api_test_cases.md

И начинаем писать:

- positive cases
- required fields validation
- negative cases
- edge cases
- business logic cases

Это станет основой для будущих API autotests.