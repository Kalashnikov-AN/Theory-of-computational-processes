package zabsu.montecarlopi;

import java.util.Random;
import java.util.function.Consumer;

/**
 * Класс модели данных для вычисления числа PI методом Монте-Карло
 */
public class MonteCarloPi {

    /**
     * Флаг выполнения вычислений.
     *
     * volatile нужен для корректной работы в многопоточности:
     *  изменения в одном потоке (UI) сразу видны в другом (фоновом)
     */
    private volatile boolean running = false;

    /** Генератор случайных чисел */
    private final Random random = new Random();

    /**
     * Метод остановки вычислений.
     * Устанавливает флаг running = false,
     * из-за чего основной цикл в calculate() завершится
     */
    public void stop() {
        running = false;
    }

    /**
     * Проверка, выполняются ли сейчас вычисления
     */
    public boolean isRunning() {
        return running;
    }

    /**
     * Метод вычисления числа PI методом Монте-Карло.
     *
     * @param iterations общее количество итераций (случайных точек)
     * @param progressCallback callback для передачи прогресса
     * @param resultCallback callback для передачи итогового результата PI
     *
     * @return вычисленное значение числа PI
     */
    public double calculate(long iterations,
                            Consumer<Double> progressCallback,
                            Consumer<Double> resultCallback) {
        running = true;
        long insideCircle = 0;
        long i = 0; // объявляем снаружи, чтобы знать реальное число итераций после остановки

        /*
         * Шаг обновления прогресса.
         */
        long progressStep = Math.max(iterations / 100, 1);

        for (; i < iterations && running; i++) {

            // Генерация случайной точки
            double x = random.nextDouble();
            double y = random.nextDouble();

            // Проверка попадания внутрь четверти круга
            if (x * x + y * y <= 1) {
                insideCircle++;
            }

            /**
             * Обновляем прогресс при достижении
             * очередного процента выполнения.
             */
            if (i % progressStep == 0) {

                // Прогресс в диапазоне [0..1]
                double progress = (double) i / iterations;

                // Передаём прогресс наружу
                progressCallback.accept(progress);
            }
        }

        // Обновляем прогресс до финального значения после завершения цикла
        // (1.0 при нормальном завершении, меньше — если остановили)
        double finalProgress = (iterations > 0) ? (double) i / iterations : 0.0;
        progressCallback.accept(finalProgress); //todo: в цикле использовать изменение по одному проценту, для каждого запуска считать 1 процент


        // делим на i (реально выполненные итерации)
        double pi = (i > 0) ? 4.0 * insideCircle / i : 0.0;
        resultCallback.accept(pi); // передаём результат наружу
        running = false;
        return pi;
    }
}