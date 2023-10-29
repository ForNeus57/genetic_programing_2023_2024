package genetic.algorithims.tinygp.fitness;

import genetic.algorithims.tinygp.individual.Individual;


/**
 * TODO: make variable number and fitness cases variable obs-elite, due to the fact that that double be ArrayList<ArrayList<Double>>
 */
public class Calculator {
    private final int variableNumber;
    private final int fitnessCases;
    private final double [][] targets;
    private final double [] x;

    public Calculator(int variableNumber, int fitnessCases, double[][] targets, double[] x) {
        this.variableNumber = variableNumber;
        this.fitnessCases = fitnessCases;
        this.targets = targets;
        this.x = x;
    }

    public double calculateFitness(Individual program) {
        double fit = 0.0;

        for (int i = 0; i < this.fitnessCases; i++) {
            if (this.variableNumber >= 0)      //  Isn't it always true, because variable number cannot be 0, since it would be constant function.
                System.arraycopy(this.targets[i], 0, x, 0, this.variableNumber);

            var interpreter = new Interpreter(program, x);
            fit += Math.abs(interpreter.run() - this.targets[i][this.variableNumber]);
        }
        return -fit;
    }

}
