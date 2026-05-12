package zabsu.n_threads_integration;

/**
 * Функциональный интерфейс для представления математической функции f(x)
 */
@FunctionalInterface
public interface MathFunction {

    /**
     * Вычисляет значение функции в точке x.
     *
     * @param x аргумент функции
     * @return значение функции f(x)
     */
    double apply(double x);
}