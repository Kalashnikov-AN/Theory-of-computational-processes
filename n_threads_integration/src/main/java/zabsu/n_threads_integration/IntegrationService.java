package zabsu.n_threads_integration;

/**
 * Сервисный класс, реализующий параллельное численное интегрирование методом прямоугольников.
 *
 *  Задача разбивается на несколько подзадач.
 *  Каждая подзадача выполняется в отдельном потоке.
 *  Частичные результаты суммируются в общей переменной.
 */
public class IntegrationService {

    /**
     * Общая переменная для накопления результата
     * Используется всеми потоками
     */
    private double result = 0.0;

    /**
     * Выполняет параллельное интегрирование.
     *
     * @param model       модель задачи (границы, функция, разбиение)
     * @param threadCount количество потоков
     * @return приближённое значение интеграла
     */
    public double integrate(IntegrationModel model, int threadCount) throws InterruptedException {

        double a = model.getA(); // начало интервала
        double b = model.getB(); // конец интервала
        int n = model.getN();    // количество разбиений

        // Шаг интегрирования, длина каждого прямоугольника
        double h = (b - a) / n;
//todo: разделить логику интегрирования  и многопоточности разные классы
        // Массив потоков
        Thread[] threads = new Thread[threadCount]; // ссылки на thread

        result = 0.0;

        int start = 0;

        // Создание потоков
        for (int t = 0; t < threadCount; t++) {

            // Размер подзадачи (сколько итераций на поток)
            int chunk = n / threadCount;

            // Первые (n % threadCount) потоков получают +1 итерацию,
            // равномерно распределяя остаток от деления
            if (t < n % threadCount) chunk = chunk + 1;
//todo: architecture simpler
            int end = start + chunk;

            final int threadStart = start;

            // Создание потока
            threads[t] = new Thread(() -> { // выделение памяти, записываем объект Thread

                // Вычисление локальной суммы для участка [threadStart, end)
                double localSum = computePartialSum(model, a, h, threadStart, end);

                /*
                 * Мьютекс
                 * Добавление локального результата в общий result
                 * Только один поток может выполнять этот блок
                 * Это предотвращает неопределённость параллелизма
                 */
                synchronized (this) {
                    result += localSum;
                }
            });

            threads[t].start();

            start = start + chunk;
        }

        for (Thread thread : threads) {
            thread.join();
        }

        /*
         * Финальный результат:
         * сумма * шаг интегрирования
         */
        return result * h;
    }


    /**
     * Вычисляет частичную сумму методом прямоугольников для заданного участка разбиения
     *
     * @param model модель задачи (содержит функцию f(x))
     * @param a     левая граница всего интервала интегрирования
     * @param h     шаг интегрирования
     * @param start начало участка
     * @param end   конец участка(не включая)
     * @return сумма значений функции f(x)
     */
    double computePartialSum(IntegrationModel model, double a, double h, int start, int end) {
        double localSum = 0.0;

        for (int i = start; i < end; i++) {

            // вычисление точки
            double x = a + i * h;

            // суммирование значений функции
            localSum += model.f(x);
        }

        return localSum;
    }
}
