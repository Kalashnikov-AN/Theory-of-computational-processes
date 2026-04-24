package zabsu.n_threads_integration;


public class IntegrationModel {

    private double a;
    private double b;
    private int n;
    private MathFunction function;

    public IntegrationModel(double a, double b, int n, MathFunction function) {
        this.a = a;
        this.b = b;
        this.n = n;
        this.function = function;
    }

    public double getA() { return a; }
    public double getB() { return b; }
    public int getN() { return n; }

    public double f(double x) {
        return function.apply(x);
    }
}