package genetic.data.functions;

import static java.lang.Math.pow;

public class function {
    public double calculate(double x) {
        return 5 * pow(x, 3) - 2 * pow(x, 2) + 3 * x - 17;
    }
}
