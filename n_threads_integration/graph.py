import matplotlib.pyplot as plt

threads = [1, 2, 4, 8]
times = [1200, 650, 400, 380]

# идеальное ускорение
ideal = [times[0] / t for t in threads]

plt.figure()

plt.plot(threads, times, marker='o', label="Реальное время")
plt.plot(threads, ideal, linestyle='--', label="Идеальное")

plt.xlabel("Потоки")
plt.ylabel("Время (ms)")
plt.title("Реальное vs идеальное ускорение")

plt.legend()
plt.grid()

plt.show()