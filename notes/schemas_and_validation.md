# FastAPI Architecture Notes

## BaseModel

`BaseModel` — это базовый класс из библиотеки Pydantic.

Используется для:

* валидации данных
* проверки request / response body
* сериализации JSON
* автоматической генерации Swagger documentation

### Пример

```python
class CourseBase(BaseModel):
    title: str
    description: str
    is_active: bool = True
```

### CourseCreate

`CourseCreate` — схема для request body при создании курса через `POST /courses`.

```python
class CourseCreate(CourseBase):
    pass
```

`CourseCreate` наследуется от `CourseBase`, поэтому автоматически получает поля:

* `title`
* `description`
* `is_active`

`pass` означает, что класс пока ничего нового не добавляет.

То есть схема полностью повторяет `CourseBase`.

Пример request body:

```json
{
  "title": "Python QA",
  "description": "API testing",
  "is_active": true
}
```

---

### CourseResponse

`CourseResponse` — схема для response body.

```python
class CourseResponse(CourseBase):
    id: int
```

Она наследует поля из `CourseBase` и дополнительно добавляет `id`.

`id` не передается клиентом при создании курса.
Обычно `id` генерирует backend или database.

Пример response body:

```json
{
  "id": 1,
  "title": "Python QA",
  "description": "API testing",
  "is_active": true
}
```

---

### Главное правило

`CourseCreate` описывает то, что клиент отправляет в API.

`CourseResponse` описывает то, что API возвращает клиенту.

---

## from_attributes = True

`from_attributes = True` используется в response schema.

Он говорит Pydantic, что данные можно брать не только из обычного словаря, но и из атрибутов объекта.

Например, обычный dict:

```python
{
    "id": 1,
    "title": "Python QA"
}
```

ORM object / SQLAlchemy object:

```python
course.id
course.title
course.description
course.is_active
```

Без `from_attributes = True` Pydantic ожидает данные как словарь.

С `from_attributes = True` Pydantic может взять данные из объекта и превратить их в JSON response.

### Зачем это нужно

Когда backend получает курс из базы данных, SQLAlchemy обычно возвращает объект, а не словарь.

Например:

```python
course.id
course.title
course.description
course.is_active
```

А клиенту API должен вернуть JSON:

```json
{
  "id": 1,
  "title": "Python QA",
  "description": "API testing",
  "is_active": true
}
```

`from_attributes = True` помогает преобразовать ORM object в response schema.

### Как объяснить на собесе

`from_attributes = True` нужен, чтобы Pydantic мог создавать response schema из ORM objects, например из SQLAlchemy model.

То есть Pydantic берет значения из атрибутов объекта:

```python
course.id
course.title
course.description
```

и превращает их в JSON response.

Это означает, что API ожидает JSON примерно такого вида:

```json
{
  "title": "Python QA",
  "description": "API testing",
  "is_active": true
}
```

---

## Что означает каждое поле

### `title: str`

* обязательное поле
* должно быть строкой (`string`)

### `description: str`

* обязательное поле
* тоже строка

### `is_active: bool = True`

* boolean поле (`true / false`)
* значение по умолчанию = `True`

Это значит:

если клиент не отправил поле `is_active`, FastAPI сам подставит:

```json
"is_active": true
```

### Пример запроса без `is_active`

```json
{
  "title": "Python QA",
  "description": "API testing"
}
```

Сервер внутри обработает это как:

```json
{
  "title": "Python QA",
  "description": "API testing",
  "is_active": true
}
```

---

## Если убрать `= True`

```python
is_active: bool
```

Тогда поле становится обязательным.

Если клиент не отправит его — API вернет ошибку:

```json
422 Unprocessable Entity
```

---

## Простое правило

### Есть `=`

→ поле optional (есть default value)

### Нет `=`

→ поле required

---

## Если написать `= False`

```python
is_active: bool = False
```

Тогда FastAPI будет автоматически подставлять:

```json
"is_active": false
```

Это удобно, если по бизнес-логике курс после создания должен быть неактивным, пока его не подтвердит админ.