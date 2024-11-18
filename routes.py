# Определяет маршруты API для конвертации валют.
# Обрабатывает входящие запросы и вызывает методы конвертера валют.

from fastapi import APIRouter, Query, HTTPException
from services.currency import CurrecyConverter

router = APIRouter()
converter = CurrecyConverter()


@router.get("/api/rates/")
async def convert(
    from_currency: str = Query(..., description="Код исходной валюты"),
    to_currency: str = Query(..., description="Код валюты назначения"),
    amount: float = Query(..., gt=0, description="Сумма конвертации"),
) -> dict:
    """
    Конвертирует указанную сумму из одной валюты в другую.

    :param from_currency: Код исходной валюты.
    :param to_currency: Код валюты назначения.
    :param amount: Сумма конвертации.
    :return: Словарь с результатом конвертации.
    """
    try:
        result = await converter.convert(from_currency, to_currency, amount)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
