package zabsu.n_threads_integration;

/**
 * Отвечает за разбивку задачи интегрирования на подзадачи
 * и их параллельное выполнение
 */
public class TaskSplitter {

    /// Реализация вычисления частичной суммы
    private final PartialSumCalculator calculator;

    /// Конструктор по умолчанию - использует IntegrationService как реализацию частичной суммы
    public TaskSplitter() {
        this.calculator = new IntegrationService();
    }

    /**
     * Конструктор с параметрами
     * @param calculator реализация вычисления частичной суммы
     */
    public TaskSplitter(PartialSumCalculator calculator) {
        this.calculator = calculator;
    }

    /**
     * Общая переменная для накопления результата
     */
    private double result = 0.0;

    /**
     * Разбивает задачу на части, запускает потоки и возвращает итоговое значение интеграла
     *
     * @param model       модель задачи
     * @param threadCount количество потоков
     * @return приближённое значение интеграла
     * @throws IllegalArgumentException если threadCount <= 0
     */
    public double computeParallel(IntegrationModel model, int threadCount) throws InterruptedException {
        if (threadCount <= 0) {
            throw new IllegalArgumentException("Количество потоков должно быть больше нуля");
        }

        int n    = model.getN();
        double a = model.getA();
        double h = (model.getB() - model.getA()) / n;

        // Массив потоков
        Thread[] threads = new Thread[threadCount]; // ссылки на thread

        result = 0.0;

        int start = 0;

        for (int t = 0; t < threadCount; t++) {

            // Размер подзадачи (сколько итераций на поток)
            int chunk = n / threadCount;

            // Первые (n % threadCount) потоков получают +1 итерацию,
            // равномерно распределяя остаток от деления
            if (t < n % threadCount)
                chunk++;

            int end = start + chunk;

            final int threadStart = start;
            final int threadEnd   = end;

            // Создание потока
            threads[t] = new Thread(() -> { // выделение памяти, записываем объект Thread

                // Локальную суммму вычислит выбранный класс
                double localSum = calculator.computePartialSum(model, a, h, threadStart, threadEnd);

                /*
                 * Мьютекс: только один поток единовременно обновляет общий результат
                 * Предотвращает неопределённость параллелизма при записи в result
                 */
                synchronized (this) {
                    result += localSum;
                }
            });

            threads[t].start();
            start = end;
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
}