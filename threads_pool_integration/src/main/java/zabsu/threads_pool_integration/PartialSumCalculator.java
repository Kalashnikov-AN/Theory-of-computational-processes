package zabsu.threads_pool_integration;

public interface PartialSumCalculator {
    double computePartialSum(IntegrationModel model, double a, double h, int start, int end);
}
