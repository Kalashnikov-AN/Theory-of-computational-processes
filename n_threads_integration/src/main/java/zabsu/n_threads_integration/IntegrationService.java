package zabsu.n_threads_integration;

/**
 * Сервис, отвечающий за математическую логику численного интегрирования
 *
 * Реализует функицональный интерфейс PartialSumCalculator
 *
 * Не знает ничего о потоках — только вычисляет
 */
public class IntegrationService implements PartialSumCalculator {

    /**
     * Вычисляет частичную сумму методом прямоугольников для участка [start, end)
     *
     * @param model модель задачи
     * @param a     левая граница всего интервала
     * @param h     шаг интегрирования
     * @param start начальный индекс разбиения
     * @param end   конечный индекс разбиения (не включая)
     * @return сумма значений f(x) на участке
     */
    @Override
    public double computePartialSum(IntegrationModel model, double a, double h, int start, int end) {
        double localSum = 0.0;
        for (int i = start; i < end; i++) {
            localSum += model.f(a + i * h);
        }
        return localSum;
    }
}