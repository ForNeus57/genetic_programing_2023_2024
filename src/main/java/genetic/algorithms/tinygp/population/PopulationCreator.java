package genetic.algorithms.tinygp.population;

import genetic.algorithms.tinygp.individual.Individual;
import genetic.algorithms.tinygp.individual.IndividualCreator;
import genetic.data.InputData;

import java.util.ArrayList;
import java.util.Random;

public class PopulationCreator {

    public static final int populationSize = 100000;
    private final InputData data;

    public PopulationCreator(InputData inputData) {
        this.data = inputData;
    }

    public Population createRandomPopulation(int maxLength, Random randomDevice) {
        ArrayList<Individual> populationHolder = new ArrayList<>();

        var creator = new IndividualCreator(
            maxLength,
            randomDevice,
            this.data.header().variableNumber(),
            this.data.header().randomConstraintsSize()
        );

        //  TODO: Rewrite it to be better.
        for (int i = 0; i < populationSize; ++i) {
            populationHolder.add(creator.createRandomIndividual());
        }

        return new Population(populationHolder);
    }
}
