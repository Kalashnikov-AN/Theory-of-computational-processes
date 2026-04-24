package zabsu.n_threads_integration;

public class IntegrationService {

    private double result = 0.0;

    public double integrate(IntegrationModel model, int threadCount) throws InterruptedException {
        double a = model.getA();
        double b = model.getB();
        int n = model.getN();

        double h = (b - a) / n;

        Thread[] threads = new Thread[threadCount];

        int chunk = n / threadCount;

        result = 0.0;

        for (int t = 0; t < threadCount; t++) {
            int start = t * chunk;
            int end = (t == threadCount - 1) ? n : start + chunk;

            threads[t] = new Thread(() -> {
                double localSum = 0.0;

                for (int i = start; i < end; i++) {
                    double x = a + i * h;
                    localSum += model.f(x);
                }

                // СИНХРОНИЗАЦИЯ (мьютекс)
                synchronized (this) {
                    result += localSum;
                }
            });

            threads[t].start();
        }

        for (Thread thread : threads) {
            thread.join();
        }

        return result * h;
    }
}
