# Routes and Routers

## Что такое route

`route` — это путь API, по которому клиент может отправить запрос.

Например:

```http
POST /courses
```

Это значит:

клиент отправляет запрос на создание курса.

---

## Что такое endpoint

`endpoint` — это конкретная функция backend, которая обрабатывает запрос по определенному route.

Например:

```python
@router.post("/courses")
def create_course(course: CourseCreate):
    return {
        "message": "Course created successfully",
        "data": course
    }
```

Здесь:

* `@router.post("/courses")` — route
* `create_course()` — endpoint function
* `course: CourseCreate` — request body schema
* `return ...` — response body

---

## Что такое APIRouter

`APIRouter` — это инструмент FastAPI для разделения endpoint'ов по логическим модулям.

Например:

```python
from fastapi import APIRouter

router = APIRouter()
```

Он нужен, чтобы не писать все endpoints в одном `main.py`.

---

## Почему не писать всё в main.py

Если писать всё в `main.py`, файл быстро станет большим и неудобным.

Например:

```python
@app.post("/courses")
@app.get("/courses")
@app.put("/courses/{course_id}")
@app.delete("/courses/{course_id}")

@app.post("/users")
@app.get("/users")

@app.post("/auth/login")
@app.post("/payments")
```

Такой код сложно поддерживать.

---

## Как лучше

Разделять routes по файлам:

```text
app/
├── main.py
├── routes/
│   └── course.py
├── schemas/
│   └── course.py
└── models/
```

Например:

* `routes/course.py` — endpoints для courses
* `routes/user.py` — endpoints для users
* `routes/auth.py` — endpoints для auth
* `routes/payment.py` — endpoints для payments

---

## Наш пример `routes/course.py`

```python
from fastapi import APIRouter
from app.schemas.course import CourseCreate

router = APIRouter()


@router.post("/courses")
def create_course(course: CourseCreate):
    return {
        "message": "Course created successfully",
        "data": course
    }
```

---

## Что здесь происходит

### `from fastapi import APIRouter`

Импортируем `APIRouter` из FastAPI.

---

### `from app.schemas.course import CourseCreate`

Импортируем schema, которая описывает request body для создания курса.

То есть FastAPI будет ожидать JSON по структуре `CourseCreate`.

---

### `router = APIRouter()`

Создаем отдельный router для группы endpoints.

В нашем случае — для courses.

---

### `@router.post("/courses")`

Говорим FastAPI:

этот endpoint должен обрабатывать `POST` запросы на путь:

```http
/courses
```

---

### `def create_course(course: CourseCreate):`

Создаем функцию, которая будет выполняться при запросе на `POST /courses`.

`course: CourseCreate` значит:

тело запроса должно соответствовать schema `CourseCreate`.

Пример request body:

```json
{
  "title": "Python QA",
  "description": "API testing",
  "is_active": true
}
```

FastAPI автоматически:

* прочитает JSON body
* проверит обязательные поля
* проверит типы данных
* создаст объект `course`
* передаст его в функцию `create_course`

---

### `return {...}`

Это response body.

Например:

```json
{
  "message": "Course created successfully",
  "data": {
    "title": "Python QA",
    "description": "API testing",
    "is_active": true
  }
}
```

---

## router vs app

### `app = FastAPI()`

Это всё приложение целиком.

Обычно находится в `main.py`.

---

### `router = APIRouter()`

Это отдельная группа endpoint'ов.

Например:

* router для courses
* router для users
* router для auth
* router для payments

---

## include_router()

`include_router()` используется для подключения отдельного APIRouter к основному приложению FastAPI.

Пример:

```python
from app.routes.course import router as course_router

app.include_router(course_router)
```

---

## Что это значит

`router` — это отдельная группа endpoint'ов.

Например:

* courses
* users
* auth
* payments

`app` — это всё FastAPI приложение целиком.

`include_router()` говорит FastAPI:

"подключи этот router к моему приложению"

---

## Что будет без include_router()

Если не написать:

```python
app.include_router(course_router)
```

то endpoint не будет существовать.

Например:

```python
@router.post("/courses")
def create_course():
```

будет написан, но:

* Swagger его не покажет
* Postman получит 404
* endpoint фактически не работает

---

## Почему пишут `router as course_router`

```python
from app.routes.course import router as course_router
```

Это делается для читаемости.

Когда в проекте много routers:

* course_router
* user_router
* auth_router
* payment_router

сразу понятно, что именно подключается.

---

## Коротко

`route` — путь API.

`endpoint` — функция, которая обрабатывает этот путь.

`APIRouter` — способ группировать endpoints по файлам и модулям.

`include_router()` — подключает router к основному FastAPI application.

`CourseCreate` — schema, которая описывает request body для `POST /courses`.
