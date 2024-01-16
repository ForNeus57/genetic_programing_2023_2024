package genetic.algorithms.tinygp.fitness;

import genetic.algorithms.tinygp.individual.Individual;


/**
 * TODO: make variable number and fitness cases variable obs-elite, due to the fact that that double be ArrayList<ArrayList<Double>>
 */
public class Calculator {
    private final int variableNumber;
    private final double [][] targets;
    private final double [] x;

    public Calculator(int variableNumber, double[][] targets, double[] x) {
        this.variableNumber = variableNumber;
        this.targets = targets;
        this.x = x;
    }

    public double calculateFitness(Individual program) {
        double fit = 0.0;

        for (double[] target : targets) {
            var tinyGPValue = calculateTinyGPValue(target, program);
            fit += Math.abs(tinyGPValue - target[this.variableNumber]);
        }
        return -fit;
    }

    public double calculateTinyGPValue(double[] target, Individual program) {
        if (this.variableNumber >= 0)      //  Isn't it always true, because variable number cannot be 0, since it would be constant function. May be it is something leftover after std::memcopy(...)
            System.arraycopy(target, 0, x, 0, this.variableNumber);

        var interpreter = new Interpreter(program, x);
        return interpreter.run();
    }
}
