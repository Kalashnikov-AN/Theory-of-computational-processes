
__author__ = "Калашников А.Н."

"""
Импортирует все функции из async_functions и запускает замеры.
"""

from async_functions import benchmark, get_urls


def main() -> None:
    RUNS   = 3
    N_MAIN = 5

    urls = get_urls(N_MAIN)


    print(f"  Запросов: {N_MAIN}  Прогонов: {RUNS}")

    r = benchmark(urls, runs=RUNS)

    print("\n   Итоги:")
    print(f"  Синхронно  — среднее: {r['sync_mean']:.3f}s  "
          f"медиана: {r['sync_median']:.3f}s")
    print(f"  Асинхронно — среднее: {r['async_mean']:.3f}s  "
          f"медиана: {r['async_median']:.3f}s")

    speedup_mean = r["sync_mean"] / r["async_mean"]
    speedup_med  = r["sync_median"] / r["async_median"]
    print(f"\n  Ускорение (по среднему):  {speedup_mean:.1f}x")
    print(f"  Ускорение (по медиане):   {speedup_med:.1f}x")



if __name__ == "__main__":
    main()





"""
Итоги:
  Синхронно  — среднее: 1.353s  медиана: 1.424s
  Асинхронно — среднее: 0.627s  медиана: 0.627s

  Ускорение (по среднему):  2.2x
  Ускорение (по медиане):   2.3x
"""