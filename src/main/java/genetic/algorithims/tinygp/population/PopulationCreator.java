package genetic.algorithims.tinygp.population;

import genetic.algorithims.tinygp.individual.Individual;
import genetic.algorithims.tinygp.individual.IndividualCreator;
import genetic.data.InputData;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class PopulationCreator {

    private final int populationSize;
    private final InputData data;

    public PopulationCreator(int populationSize, InputData inputData) {
        this.populationSize = populationSize;
        this.data = inputData;
    }

    public Population createRandomPopulation(int maxLength, Random randomDevice, int maxDepth) {
        ArrayList<Individual> populationHolder = new ArrayList<>();

        var creator = new IndividualCreator(
            maxLength,
            randomDevice,
            maxDepth,
            this.data.header().variableNumber(),
            this.data.header().randomConstraintsSize()
        );

        //  TODO: Rewrite it to be better.
        for (int i = 0; i < this.populationSize; ++i) {
            populationHolder.add(creator.createRandomIndividual());
        }

        return new Population(populationHolder);
    }
}
