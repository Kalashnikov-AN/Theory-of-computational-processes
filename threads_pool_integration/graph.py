import matplotlib.pyplot as plt

threads = [1, 2, 3, 4, 5, 6]
times = [8150, 3991, 2678, 2054, 1690, 1474]

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