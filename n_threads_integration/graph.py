import matplotlib.pyplot as plt

threads = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
times = [12973, 7589, 6162, 4570, 3930, 3424, 3025, 2668, 2408, 2189, 2122, 2089]

# идеальное ускорение
ideal = [times[0] / t for t in threads]

plt.figure()

plt.plot(threads, times, marker='o', label="Реальное время")
plt.plot(threads, ideal, linestyle='--', marker = 'o', label="Идеальное")

plt.xlabel("Потоки")
plt.ylabel("Время (ms)")
plt.title("Реальное vs идеальное ускорение")

plt.legend()
plt.grid()

plt.show()