# Содержит класс CurrecyConverter, который отвечает за обновление курсов валют
# и выполнение конвертации между валютами, используя внешний API.

import aiohttp
from typing import Dict, List
from config import settings


class CurrecyConverter:

    API_URL = settings.API_URL

    def __init__(self) -> None:
        self.rates: Dict[str, float] = {}

    async def update_rates(self, source: str = "USD",
                           currencies: List[str] = None) -> None:
        """Получает актуальные курсы валют из API."""
        params = {"source": source}
        if currencies:
            params["currencies"] = ",".join(currencies)
        async with aiohttp.ClientSession() as session:
            async with session.get(self.API_URL, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    if "quotes" in data:
                        self.rates[source] = {
                            key[len(source):]: value
                            for key, value in data["quotes"].items()
                            if key.startswith(source)
                        }
                    else:
                        raise ValueError("Ошибка в данных API:"
                                         "'quotes' не найдено.")
                else:
                    raise ConnectionError(f"Ошибка при запросе API:"
                                          f"{response.text}")

    async def convert(
            self,
            from_currency: str,
            to_currency: str,
            amount: float
            ) -> float:
        """
        Конвертирует сумму из одной валюты в другую.

        :param from_currency: Код исходной валюты.
        :param to_currency: Код валюты назначения.
        :param amount: Сумма конвертации.
        :return: Конвертированная сумма.
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates:
            await self.update_rates(source=from_currency)

        if to_currency not in self.rates[from_currency]:
            raise ValueError(f"Курс для {to_currency} недоступен.")

        rate = self.rates[from_currency][to_currency]
        return round(amount * rate, 2)
