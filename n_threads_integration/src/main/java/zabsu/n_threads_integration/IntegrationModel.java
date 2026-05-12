package zabsu.n_threads_integration;

/**
 * Модель данных для задачи численного интегрирования
 */
public class IntegrationModel {

    /**
     * Нижняя граница интегрирования.
     */
    private double a;

    /**
     * Верхняя граница интегрирования.
     */
    private double b;

    /**
     * Количество разбиений интервала.
     *
     * интервал [a, b] делится на n частей
     * шаг интегрирования: h = (b - a) / n
     */
    private int n;

    /**
     * Функция, которую нужно интегрировать.
     *
     * Представлена через функциональный интерфейс MathFunction.
     */
    private MathFunction function;

    /**
     * Конструктор модели.
     *
     * @param a        левая граница
     * @param b        правая граница
     * @param n        количество разбиений
     * @param function функция f(x) //todo: exception
     */
    public IntegrationModel(double a, double b, int n, MathFunction function) {
        // Проверка, что функция не null
        if (function == null) {
            throw new IllegalArgumentException("Функция не может быть null");
        }
        // Количество разбиений должно быть положительным
        if (n <= 0) {
            throw new IllegalArgumentException("Количество разбиений должно быть больше нуля");
        }
        // Нижняя граница должна быть строго меньше верхней
        if (a >= b) {
            throw new IllegalArgumentException("Нижняя граница (a) должна быть меньше верхней (b)");
        }
        // Дополнительная проверка на NaN и бесконечности
        if (Double.isNaN(a) || Double.isNaN(b) || Double.isInfinite(a) || Double.isInfinite(b)) {
            throw new IllegalArgumentException("Границы интегрирования должны быть конечными числами");
        }

        this.a = a;
        this.b = b;
        this.n = n;
        this.function = function;
    }

    /**
     * @return левая граница интегрирования
     */
    public double getA() { return a; }

    /**
     * @return правая граница интегрирования
     */
    public double getB() { return b; }

    /**
     * @return количество разбиений интервала
     */
    public int getN() { return n; }

    /**
     * Вычисляет значение функции в точке x.
     *
     * @param x точка, в которой нужно вычислить функцию
     * @return f(x)
     */
    public double f(double x) {
        return function.apply(x);
    }
}