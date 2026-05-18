package zabsu.threads_pool_integration;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

/**
 * Отвечает за разбивку задачи интегрирования на подзадачи
 * и параллельное их выполнение через пул потоков
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
     * Разбивает задачу на части, запускает пул потоков и возвращает итоговую сумму.
     *
     * @param model       модель задачи
     * @param threadCount количество потоков в пуле
     * @return приближённое значение интеграла
     */
    public double computeParallel(IntegrationModel model, int threadCount)
            throws InterruptedException, ExecutionException {

        int n    = model.getN();
        double a = model.getA();
        double h = (model.getB() - model.getA()) / n;

        // Создаём пул фиксированного размера
        ExecutorService executor = Executors.newFixedThreadPool(threadCount);

        int tasks = threadCount * 2; // можем сделать кол-во подзадач больше, чем число потоков

        List<Future<Double>> futures = new ArrayList<>(tasks); // список задач, которые вернут Double

        int start = 0;

        for (int t = 0; t < tasks; t++) {

            int chunk = n / tasks;

            // Первые (n % tasks) потоков получают +1 итерацию,
            // равномерно распределяя остаток от деления
            if (t < n % tasks)
                chunk++;

            int end = start + chunk;

            final int threadStart = start;
            final int threadEnd   = end;

            // Каждая подзадача — Callable, возвращающий частичную сумму
            futures.add(executor.submit(
                    () -> calculator.computePartialSum(model, a, h, threadStart, threadEnd)
            ));

            start = end;
        }

        // Завершаем приём новых задач
        executor.shutdown();

        // Собираем результаты из Future — каждый поток вернул свою локальную сумму
        double total = 0.0;
        for (Future<Double> future : futures) {
            total += future.get();
        }

        return total * h;
    }

}
