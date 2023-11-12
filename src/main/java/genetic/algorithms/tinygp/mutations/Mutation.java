package genetic.algorithms.tinygp.mutations;

import genetic.algorithms.tinygp.individual.Individual;

import java.util.Random;

import static genetic.algorithms.tinygp.TinyGP.FSET_END;
import static genetic.algorithms.tinygp.TinyGP.FSET_START;

public class Mutation {

    public final static double ProbabilityOfMutationPerNode = 0.05;

    private final Random randomDevice;
    private final int variableNumber;
    private final int randomConstraintsSize;

    public Mutation(Random randomDevice, int variableNumber, int randomConstraintsSize) {
        this.randomDevice = randomDevice;
        this.variableNumber = variableNumber;
        this.randomConstraintsSize = randomConstraintsSize;
    }

    public Individual mutation(Individual parent) {
        int len = parent.size();
        char [] parentCopy = new char [len];

        System.arraycopy(parent.body(), 0, parentCopy, 0, len);
        for (int i = 0; i < len; i++) {
            if (this.randomDevice.nextDouble() < Mutation.ProbabilityOfMutationPerNode) {
                if (parentCopy[i] < FSET_START)     // If a parentCopy[i] is a variable, then replace it with a random variable.
                    parentCopy[i] = (char) this.randomDevice.nextInt(this.variableNumber + this.randomConstraintsSize);
                else    // If a parentCopy[i] is a function, then replace it with a random function.
                    parentCopy[i] = (char) (this.randomDevice.nextInt(FSET_END - FSET_START + 1) + FSET_START);
            }
        }
        return new Individual(parentCopy);
    }
}
