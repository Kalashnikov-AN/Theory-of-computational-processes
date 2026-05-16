package zabsu.n_threads_integration;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Тесты для IntegrationService
 */
public class IntegrationServiceTest {

    /**
     * Проверка computePartialSum()
     *
     * Интегрируем f(x) = x^2
     * на участке [0, 1]
     */
    @Test
    void testComputePartialSum() {

        IntegrationService service = new IntegrationService();

        MathFunction function = x -> x * x;

        IntegrationModel model = new IntegrationModel(0, 1, 10, function);

        double h = 0.1;

        double expected = 0.30; // 0.00 + 0.01 + 0.04 + 0.09 + 0.16 = 0.30

        double actual = service.computePartialSum(model, 0, h, 0, 5);

        assertEquals(expected, actual, 1e-9);
    }

    /**
     * Проверка интегрирования sin(x)
     *
     * (sin(x) от 0 до PI) == 2
     */
    @Test
    void testIntegrateSin() throws InterruptedException {

        TaskSplitter splitter = new TaskSplitter();

        IntegrationModel model =
                new IntegrationModel(0, Math.PI, 1_000_000, Math::sin);

        double result = splitter.computeParallel(model, 4);

        assertEquals(2.0, result, 1e-3);
    }

    /**
     * Проверка интегрирования x^2
     *
     * x^2 от 0 до 1 == 1/3
     */
    @Test
    void testIntegrateSquareFunction() throws InterruptedException {

        TaskSplitter splitter = new TaskSplitter();

        IntegrationModel model =
                new IntegrationModel(0, 1, 1_000_000, x -> x * x);

        double result = splitter.computeParallel(model, 8);

        assertEquals(1.0 / 3.0, result, 1e-4);
    }

    /**
     * Проверка одинакового результата
     * при разном количестве потоков
     */
    @Test
    void testDifferentThreadCounts() throws InterruptedException {

        TaskSplitter splitter = new TaskSplitter();

        IntegrationModel model =
                new IntegrationModel(0, Math.PI, 1_000_000, Math::cos);

        double result1 = splitter.computeParallel(model, 1);

        double result2 = splitter.computeParallel(model, 2);

        double result4 = splitter.computeParallel(model, 4);

        double result8 = splitter.computeParallel(model, 8);

        assertEquals(result1, result2, 1e-6);

        assertEquals(result1, result4, 1e-6);

        assertEquals(result1, result8, 1e-6);
    }

    /**
     * Проверка работы на большом количестве потоков
     */
    @Test
    void testManyThreads() throws InterruptedException {

        TaskSplitter splitter = new TaskSplitter();

        IntegrationModel model =
                new IntegrationModel(0, 10, 10_000_000, Math::exp);

        double result = splitter.computeParallel(model, 12);

        // Точное значение интеграла e^x на [0, 10] равно e^10 - 1
        double exact = Math.exp(10) - 1.0;


        assertEquals(exact, result, 0.1);

    }
}