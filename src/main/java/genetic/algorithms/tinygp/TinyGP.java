package genetic.algorithms.tinygp;

/*
 * Program:   tiny_gp.java
 *
 * Author:    Riccardo Poli (email: rpoli@essex.ac.uk)
 *
 */

import genetic.algorithms.tinygp.fitness.Calculator;
import genetic.algorithms.tinygp.individual.Individual;
import genetic.algorithms.tinygp.individual.IndividualCreator;
import genetic.algorithms.tinygp.individual.IndividualPrinter;
import genetic.algorithms.tinygp.mutations.Crossover;
import genetic.algorithms.tinygp.mutations.Mutation;
import genetic.algorithms.tinygp.population.Population;
import genetic.algorithms.tinygp.population.PopulationCreator;
import genetic.algorithms.tinygp.statistics.ConfigurationStatistics;
import genetic.algorithms.tinygp.statistics.Statistics;
import genetic.data.InputData;

import java.util.*;

public class TinyGP {
    double [] fitness;
    private final Population population;
    static Random rd = new Random();
    public static final int ADD = 110;
    public static final int SUB = 111;
    public static final int MUL = 112;
    public static final int DIV = 113;
    public static final int SIN = 114;
    public static final int COS = 115;
    public static final int FSET_START = ADD;
    public static final int FSET_END = COS;
    static double [] x = new double[FSET_START];
    static double fbestpop = 0.0, favgpop = 0.0;
    long seed;
    static double avg_len;
    static final int
            MAX_LEN = 10000,
            GENERATIONS = 100, //   Change so the learning process doesn't take too long.
            TSIZE = 2;
    public static final double
            CROSSOVER_PROB = 0.9;
    private final InputData inputData;
    private final ArrayList<Statistics> performanceHistory;
    public final StringBuilder output;

    void stats(double [] fitness, int gen) {
        int i, best = rd.nextInt(PopulationCreator.populationSize);
        int node_count = 0;
        fbestpop = fitness[best];
        favgpop = 0.0;

        for (i = 0; i < PopulationCreator.populationSize; i++) {
            node_count += this.population.population().get(i).size();
            favgpop += fitness[i];
            if (fitness[i] > fbestpop) {
                best = i;
                fbestpop = fitness[i];
            }
        }
        avg_len = (double) node_count / PopulationCreator.populationSize;
        favgpop /= PopulationCreator.populationSize;

        //  Print the best individual -- get the string representation of him....
        //  TODO: Make this overload the .toString() method of Individual class.
        var printer = new IndividualPrinter(this.population.population().get(best), x, this.inputData.header().variableNumber());

        var statistic = new Statistics(gen, (-favgpop), (-fbestpop), avg_len, printer.print(), this.population.population().get(best), x);
        this.performanceHistory.add(statistic);
        System.out.print(statistic);
        this.output.append(statistic);
    }

    int tournament(double [] fitness) {
        int best = rd.nextInt(PopulationCreator.populationSize), competitor;
        double  fbest = -1.0e34;

        for (int i = 0; i < TinyGP.TSIZE; ++i) {
            competitor = rd.nextInt(PopulationCreator.populationSize);
            if (fitness[competitor] > fbest) {
                fbest = fitness[competitor];
                best = competitor;
            }
        }
        return best;
    }

    int negative_tournament(double [] fitness) {
        int worst = rd.nextInt(PopulationCreator.populationSize), competitor;
        double fworst = 1e34;

        for (int i = 0; i < TinyGP.TSIZE; ++i) {
            competitor = rd.nextInt(PopulationCreator.populationSize);
            if (fitness[competitor] < fworst) {
                fworst = fitness[competitor];
                worst = competitor;
            }
        }
        return worst;
    }

    public TinyGP(InputData input, long seed) {
        this.seed = seed;
        TinyGP.rd.setSeed(seed);

        this.inputData = input;
        this.performanceHistory = new ArrayList<>();
        this.output = new StringBuilder();

        //  Fill the x register with values....
        for (int i = 0; i < FSET_START; i++)
            x[i] = (this.inputData.header().upperRange() - this.inputData.header().lowerRange()) * rd.nextDouble() + this.inputData.header().lowerRange();

        var creator = new PopulationCreator(this.inputData);
        this.population = creator.createRandomPopulation(MAX_LEN, rd);

        //  Calculate fitness for population used by generation 0
        fitness =  new double[this.population.population().size()];
        var calculator = new Calculator(this.inputData.header().variableNumber(), this.inputData.targets(), x);
        for (int i = 0; i < this.population.population().size(); i++)
            fitness[i] = calculator.calculateFitness(this.population.population().get(i));
    }

    public ArrayList<Statistics> evolve(double precision) {
        int offspring, parent1, parent2, parent;
        char [] newind;

        var configuration = new ConfigurationStatistics(
            seed,
            MAX_LEN,
            PopulationCreator.populationSize,
            IndividualCreator.maximumTreeDepth,
            CROSSOVER_PROB,
            Mutation.ProbabilityOfMutationPerNode,
            this.inputData.header().lowerRange(),
            this.inputData.header().upperRange(),
            GENERATIONS,
            TSIZE
        );
        System.out.print(configuration);
        this.output.append(configuration);

        stats(fitness, 0);
        for (int generationNumber = 1; generationNumber < GENERATIONS; ++generationNumber) {
            if (fbestpop > precision) {
                System.out.print("PROBLEM SOLVED\n");
                this.output.append("PROBLEM SOLVED\n");
                return this.performanceHistory;
            }
            for (int indivs = 0; indivs < population.population().size(); ++indivs) {
                if (rd.nextDouble() < CROSSOVER_PROB) {
                    parent1 = tournament(fitness);
                    parent2 = tournament(fitness);
                    var cross = new Crossover(rd);
                    newind = cross.crossover(this.population.population().get(parent1), this.population.population().get(parent2)).body();
                } else {
                    parent = tournament(fitness);
                    var mutator = new Mutation(rd, this.inputData.header().variableNumber(), this.inputData.header().randomConstraintsSize());
                    newind = mutator.mutation(this.population.population().get(parent)).body();
                }
                var calculator = new Calculator(this.inputData.header().variableNumber(), this.inputData.targets(), x);
                var newfit = calculator.calculateFitness(new Individual(newind));

                offspring = negative_tournament(fitness);
                this.population.population().set(offspring, new Individual(newind));
                fitness[offspring] = newfit;
            }
            stats(fitness, generationNumber);
        }

        System.out.print("PROBLEM *NOT* SOLVED\n");
        this.output.append("PROBLEM *NOT* SOLVED\n");
        return this.performanceHistory;
    }
}