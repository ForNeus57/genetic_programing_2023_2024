package genetic.algorithims.tinygp;

/*
 * Program:   tiny_gp.java
 *
 * Author:    Riccardo Poli (email: rpoli@essex.ac.uk)
 *
 */

import genetic.algorithims.tinygp.fitness.Calculator;
import genetic.algorithims.tinygp.individual.Individual;
import genetic.algorithims.tinygp.individual.IndividualCreator;
import genetic.algorithims.tinygp.population.Population;
import genetic.algorithims.tinygp.population.PopulationCreator;
import genetic.algorithims.tinygp.statistics.ConfigurationStatistics;
import genetic.algorithims.tinygp.statistics.Statistics;
import genetic.data.InputData;

import java.util.*;

/**
 * I'm not refactoring this, it has no comments and I lack technical knowledge to do it - sorry...
 * I don't want to risk fucking something up due to some edge condition...
 * Therefore, I refactored everything around the data flow and output of an algorithm.
 */
public class TinyGP {
    double [] fitness;

    private final Population population;
    static Random rd = new Random();
    public static final int
            ADD = 110;
    public static final int SUB = 111;
    public static final int MUL = 112;
    public static final int DIV = 113;
    public static final int FSET_START = ADD;
    public static final int FSET_END = DIV;
    static double [] x = new double[FSET_START];
    static double fbestpop = 0.0, favgpop = 0.0;
    long seed;
    static double avg_len;
    static final int
            MAX_LEN = 10000,
            POPSIZE = 100000,
            DEPTH   = 5,
            GENERATIONS = 100,
            TSIZE = 2;
    public static final double
            PMUT_PER_NODE  = 0.05,
            CROSSOVER_PROB = 0.9;
    private final InputData inputData;
    private final ArrayList<Statistics> performanceHistory;

    int traverse(char [] buffer, int buffercount) {
        if (buffer[buffercount] < FSET_START)
            return ++buffercount;

        return traverse(buffer, traverse(buffer, ++buffercount));
    }


    int print_individual(char []buffer, int buffercounter) {
        int a1 = 0, a2;
        if (buffer[buffercounter] < FSET_START) {
            if (buffer[buffercounter] < this.inputData.header().variableNumber())
                System.out.print("X"+ (buffer[buffercounter] + 1) + " ");
            else
                System.out.print(x[buffer[buffercounter]]);
            return ++buffercounter;
        }
        switch (buffer[buffercounter]) {
            case ADD -> {
                System.out.print("(");
                a1 = print_individual(buffer, ++buffercounter);
                System.out.print(" + ");
            }
            case SUB -> {
                System.out.print("(");
                a1 = print_individual(buffer, ++buffercounter);
                System.out.print(" - ");
            }
            case MUL -> {
                System.out.print("(");
                a1 = print_individual(buffer, ++buffercounter);
                System.out.print(" * ");
            }
            case DIV -> {
                System.out.print("(");
                a1 = print_individual(buffer, ++buffercounter);
                System.out.print(" / ");
            }
        }
        a2 = print_individual(buffer, a1);
        System.out.print( ")");
        return a2;
    }

    void stats( double [] fitness, int gen ) {
        int i, best = rd.nextInt(POPSIZE);
        int node_count = 0;
        fbestpop = fitness[best];
        favgpop = 0.0;

        for (i = 0; i < POPSIZE; i++) {
            node_count +=  traverse(this.population.population().get(i).body(), 0);
            favgpop += fitness[i];
            if (fitness[i] > fbestpop) {
                best = i;
                fbestpop = fitness[i];
            }
        }
        avg_len = (double) node_count / POPSIZE;
        favgpop /= POPSIZE;
        var statistic = new Statistics(gen, (-favgpop), (-fbestpop), avg_len, "...");
        this.performanceHistory.add(statistic);
//        System.out.println(statistic);
        System.out.print("Generation="+gen+" Avg Fitness="+(-favgpop)+
                " Best Fitness="+(-fbestpop)+" Avg Size="+avg_len+
                "\nBest Individual: ");
        print_individual(this.population.population().get(best).body(), 0);
        System.out.print("\n");
    }

    int tournament( double [] fitness ) {
        int best = rd.nextInt(POPSIZE), i, competitor;
        double  fbest = -1.0e34;

        for (i = 0; i < TinyGP.TSIZE; i ++ ) {
            competitor = rd.nextInt(POPSIZE);
            if ( fitness[competitor] > fbest ) {
                fbest = fitness[competitor];
                best = competitor;
            }
        }
        return( best );
    }

    int negative_tournament( double [] fitness ) {
        int worst = rd.nextInt(POPSIZE), i, competitor;
        double fworst = 1e34;

        for (i = 0; i < TinyGP.TSIZE; i ++ ) {
            competitor = rd.nextInt(POPSIZE);
            if ( fitness[competitor] < fworst ) {
                fworst = fitness[competitor];
                worst = competitor;
            }
        }
        return( worst );
    }

    char [] crossover(Individual parent1, Individual parent2) {
        int xo1start, xo1end, xo2start, xo2end;
        char [] offspring;
        int len1 = traverse( parent1.body(), 0 );
        int len2 = traverse( parent2.body(), 0 );
        int lenoff;

        xo1start =  rd.nextInt(len1);
        xo1end = traverse( parent1.body(), xo1start );

        xo2start =  rd.nextInt(len2);
        xo2end = traverse( parent2.body(), xo2start );

        lenoff = xo1start + (xo2end - xo2start) + (len1-xo1end);

        offspring = new char[lenoff];

        System.arraycopy( parent1.body(), 0, offspring, 0, xo1start );
        System.arraycopy( parent2.body(), xo2start, offspring, xo1start,
                (xo2end - xo2start) );
        System.arraycopy(parent1.body(), xo1end, offspring, xo1start + (xo2end - xo2start), (len1-xo1end));

        return( offspring );
    }

    char [] mutation(Individual parent) {
        int len = traverse(parent.body(), 0 );
        int mutsite;
        char [] parentcopy = new char [len];

        System.arraycopy( parent.body(), 0, parentcopy, 0, len );
        for (int i = 0; i < len; i ++ ) {
            if ( rd.nextDouble() < TinyGP.PMUT_PER_NODE) {
                mutsite =  i;
                if ( parentcopy[mutsite] < FSET_START )
                    parentcopy[mutsite] = (char) rd.nextInt(this.inputData.header().variableNumber() + this.inputData.header().randomConstraintsSize());
                else
                    switch (parentcopy[mutsite]) {
                        case ADD, SUB, MUL, DIV -> parentcopy[mutsite] =
                                (char) (rd.nextInt(FSET_END - FSET_START + 1)
                                        + FSET_START);
                    }
            }
        }
        return parentcopy;
    }

    /**
     * Why is this constructor so low in a file.....???
     */
    public TinyGP(InputData input, long seed) {
        this.seed = seed;
        TinyGP.rd.setSeed(seed);

        this.inputData = input;
        this.performanceHistory = new ArrayList<>();

        //  Fill the x register with values....
        for ( int i = 0; i < FSET_START; i++)
            x[i] = (this.inputData.header().upperRange() - this.inputData.header().lowerRange()) * rd.nextDouble() + this.inputData.header().lowerRange();

        var creator = new PopulationCreator(TinyGP.POPSIZE, this.inputData);
        this.population = creator.createRandomPopulation(MAX_LEN, rd, DEPTH);

        //  Calculate fitness
        fitness =  new double[POPSIZE];
        var calculator = new Calculator(this.inputData.header().variableNumber(), this.inputData.header().fitnessCases(), this.inputData.targets(), x);
        for (int i = 0; i < TinyGP.POPSIZE; i++)
            fitness[i] = calculator.calculateFitness(this.population.population().get(i));
    }

    public boolean evolve(double precision) {
        int gen, indivs, offspring, parent1, parent2, parent;
        double newfit;
        char []newind;

        System.out.print(
            new ConfigurationStatistics(
                seed,
                MAX_LEN,
                POPSIZE,
                DEPTH,
                CROSSOVER_PROB,
                PMUT_PER_NODE,
                this.inputData.header().lowerRange(),
                this.inputData.header().upperRange(),
                GENERATIONS,
                TSIZE
            )
        );

        stats(fitness, 0);
        for (gen = 1; gen < GENERATIONS; gen++) {
            if (fbestpop > precision)
                return true;
            for (indivs = 0; indivs < POPSIZE; indivs++) {
                if (rd.nextDouble() < CROSSOVER_PROB) {
                    parent1 = tournament( fitness);
                    parent2 = tournament( fitness);
                    newind = crossover(this.population.population().get(parent1), this.population.population().get(parent2));
                } else {
                    parent = tournament( fitness);
                    newind = mutation(this.population.population().get(parent));
                }
                var calculator = new Calculator(this.inputData.header().variableNumber(), this.inputData.header().fitnessCases(), this.inputData.targets(), x);
                newfit = calculator.calculateFitness(new Individual(newind));

                offspring = negative_tournament( fitness);
                this.population.population().set(offspring, new Individual(newind));
                fitness[offspring] = newfit;
            }
            stats(fitness, gen);
        }
        return false;
    }
}