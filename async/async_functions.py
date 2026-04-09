
__author__ = "Калашников А.Н."

"""
async_functions — модуль с функциями синхронных и асинхронных HTTP-запросов,
а также инструментами для замера времени.
"""

import asyncio
import statistics
import time
import httpx



#  Список URL
BASE_URLS: list[str] = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
    "https://jsonplaceholder.typicode.com/posts/6",
    "https://jsonplaceholder.typicode.com/posts/7",
    "https://jsonplaceholder.typicode.com/posts/8",
    "https://jsonplaceholder.typicode.com/posts/9",
]


def get_urls(n: int) -> list[str]:
    """Вернуть список из n URL (циклически из BASE_URLS)."""
    return [BASE_URLS[i % len(BASE_URLS)] for i in range(n)]



#  Синхронная версия
def sync_fetch(urls: list[str]) -> list[int]:
    """Последовательные HTTP GET через единственный httpx.Client."""
    statuses: list[int] = []
    with httpx.Client(timeout=30) as client:
        for url in urls:
            response = client.get(url)
            print(response)
            statuses.append(response.status_code)
    return statuses


def run_sync(urls: list[str]) -> float:
    """Запустить sync_fetch, вернуть затраченное время в секундах."""
    start = time.perf_counter()
    sync_fetch(urls)
    return time.perf_counter() - start



#  Асинхронная версия
async def async_fetch(urls: list[str]) -> list[int]:
    """
    Параллельные HTTP GET через asyncio + httpx.AsyncClient.
    asyncio.create_task запускает все корутины «одновременно»;
    asyncio.gather дожидается завершения каждой —
    всё в ОДНОМ потоке ОС (event loop).
    """
    limits = httpx.Limits(max_connections=200, max_keepalive_connections=100)
    async with httpx.AsyncClient(timeout=30, limits=limits) as client:

        async def fetch_one(url: str) -> int:
            response = await client.get(url)
            print("ASYNC", response)
            return response.status_code

        tasks = [asyncio.create_task(fetch_one(url)) for url in urls]
        statuses: list[int] = await asyncio.gather(*tasks)
    return list(statuses)


def run_async(urls: list[str]) -> float:
    """Запустить async_fetch в event loop, вернуть затраченное время."""
    start = time.perf_counter()
    asyncio.run(async_fetch(urls))
    return time.perf_counter() - start



#  Замер: несколько прогонов -> среднее / медиана
def benchmark(urls: list[str], runs: int = 3) -> dict:
    """Запустить оба варианта runs раз, вернуть статистику."""
    sync_times: list[float] = []
    async_times: list[float] = []

    for i in range(1, runs + 1):
        print(f"  Прогон {i}/{runs}: ", flush = True)

        t_sync = run_sync(urls)
        sync_times.append(t_sync)
        print(f"sync={t_sync:.2f}s  ", flush = True)

        t_async = run_async(urls)
        async_times.append(t_async)
        print(f"async={t_async:.2f}s", flush = True)

    return {
        "sync_times":   sync_times,
        "async_times":  async_times,
        "sync_mean":    statistics.mean(sync_times),
        "async_mean":   statistics.mean(async_times),
        "sync_median":  statistics.median(sync_times),
        "async_median": statistics.median(async_times),
    }

