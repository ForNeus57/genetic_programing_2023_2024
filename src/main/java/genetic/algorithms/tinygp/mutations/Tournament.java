package genetic.algorithms.tinygp.mutations;


import genetic.algorithms.tinygp.individual.Individual;
import genetic.algorithms.tinygp.population.Population;
import org.apache.commons.math3.util.Pair;

import java.util.Random;

public class Tournament {
    public static final TournamentOperation classicOperation = (fitnessValue, bestFitnessValue) -> fitnessValue > bestFitnessValue;
    public static final TournamentOperation negativeOperation = (fitnessValue, bestFitnessValue) -> fitnessValue < bestFitnessValue;

    private final TournamentOperation operation;
    private final Random randomDevice;
    private final double [] fitness;
    private final Population population;
    private final int tournamentSize;


    public Tournament(TournamentOperation operation,
                      Random randomDevice,
                      double [] fitness,
                      Population population,
                      int tournamentSize) {
        this.operation = operation;
        this.randomDevice = randomDevice;
        this.fitness = fitness;
        this.population = population;
        this.tournamentSize = tournamentSize;
    }

    public Pair<Individual, Integer> tournament() {
        int best = this.randomDevice.nextInt(this.population.population().size());

        for (int i = 0; i < this.tournamentSize; ++i) {
            int competitorIndividualIndex = this.randomDevice.nextInt(this.population.population().size());
            if (this.operation.operation(fitness[competitorIndividualIndex], fitness[best])) {
                best = competitorIndividualIndex;
            }
        }
        return new Pair<>(population.population().get(best), best);
    }
}