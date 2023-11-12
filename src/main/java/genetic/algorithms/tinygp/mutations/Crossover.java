package genetic.algorithms.tinygp.mutations;

import genetic.algorithms.tinygp.individual.Individual;

import java.util.Random;

public class Crossover {
    private final Random randomDevice;

    public Crossover(Random randomDevice) {
        this.randomDevice = randomDevice;
    }

    public Individual crossover(Individual parent1, Individual parent2) {
        int xo1start, xo1end, xo2start, xo2end;
        int len1 = parent1.size();
        int len2 = parent2.size();

        xo1start =  this.randomDevice.nextInt(len1);
        xo1end = parent1.size(xo1start);

        xo2start =  this.randomDevice.nextInt(len2);
        xo2end = parent2.size(xo2start);

        int lengthOffset = xo1start + (xo2end - xo2start) + (len1 - xo1end);

        var offspring = new char[lengthOffset];

        System.arraycopy(parent1.body(), 0, offspring, 0, xo1start);
        System.arraycopy(parent2.body(), xo2start, offspring, xo1start, (xo2end - xo2start));
        System.arraycopy(parent1.body(), xo1end, offspring, xo1start + (xo2end - xo2start), (len1-xo1end));

        return new Individual(offspring);
    }
}
