# Swagger and Postman

## Что такое Swagger

`Swagger UI` — это автоматически сгенерированная документация API.

В FastAPI она обычно доступна по адресу:

```
http://127.0.0.1:8000/docs
```

Там можно:

* смотреть все endpoints
* видеть request body
* видеть response body
* проверять обязательные поля
* смотреть типы данных
* отправлять тестовые запросы прямо из браузера

Это очень удобно для QA и backend-разработчиков.

---

## Почему Swagger сам показывает JSON

FastAPI автоматически строит Swagger documentation на основе:

* endpoint functions
* Pydantic schemas (`BaseModel`)
* type hints
* HTTP methods (`GET`, `POST`, `PUT`, `DELETE`)
* response models

---

## Пример endpoint

```
@router.post("/courses")
def create_course(course: CourseCreate):
    return {
        "message": "Course created successfully",
        "data": course
    }
```

FastAPI видит:

* `POST /courses` → это endpoint
* `course: CourseCreate` → это request body schema

---

## Откуда берется request body schema

### CourseCreate

```
class CourseCreate(CourseBase):
    pass
```

### CourseBase

```
class CourseBase(BaseModel):
    title: str
    description: str
    is_active: bool = True
```

Из этого FastAPI автоматически понимает:

* какие поля должны быть
* какие поля обязательные
* какие типы данных ожидаются
* какое поле optional
* какой пример JSON показать в Swagger

---

## Пример JSON в Swagger

```
{
  "title": "string",
  "description": "string",
  "is_active": true
}
```

---

## Почему именно так

### `title: str`

→ string

### `description: str`

→ string

### `is_active: bool = True`

→ boolean поле + значение по умолчанию

Если клиент не отправит `is_active`,
FastAPI автоматически подставит:

```
"is_active": true
```

---

## Почему это важно для QA

Swagger помогает быстро проверить:

* API contract
* обязательные поля
* optional поля
* validation rules
* expected request body
* expected response body

Это сильно ускоряет API testing.

QA может сразу увидеть:

* что именно нужно отправлять
* какие поля required
* что вернет backend
* где возможна ошибка валидации

---

## Swagger vs Postman

### Swagger

Используется чтобы:

* быстро посмотреть API
* понять структуру request/response
* протестировать endpoint вручную
* проверить валидацию

### Postman

Используется для:

* полноценного API testing
* коллекций запросов
* environment variables
* auth tokens
* automated checks
* regression testing
* negative scenarios