# Currency Converter API

Currency Converter API — это RESTful сервис для конвертации валют в реальном времени. Он использует данные с API [exchangerate.host](https://exchangerate.host/) для получения актуальных курсов валют.

## Возможности

- Конвертация заданной суммы из одной валюты в другую.
- Автоматическое обновление курсов валют.

## Требования

- Docker
- Docker Compose

## Установка и запуск

### 1. Клонируйте репозиторий

git clone https://github.com/your-username/currency-converter.git
cd currency-converter

### 2. Запустите приложение с помощью Docker Compose

docker-compose up --build

Приложение будет доступно по адресу: http://localhost:8000

### 3. Остановите приложение

docker-compose down

## **Использование**

Получение сконвертированной суммы
GET /api/rates/

## Параметры запроса:

from_currency (str): Валюта исходной суммы (например, USD).
to_currency (str): Валюта для конвертации (например, RUB).
amount (float): Сумма для конвертации.

## Пример запроса:
curl "http://localhost:8000/api/rates/?from_currency=USD&to_currency=RUB&amount=1"

## Пример ответа:
{
  "result": 100.2
}
