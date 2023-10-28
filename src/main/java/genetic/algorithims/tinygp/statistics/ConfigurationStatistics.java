package genetic.algorithims.tinygp.statistics;

public record ConfigurationStatistics(
    long seed,
    int maxLength,
    int populationSize,
    int depth,
    double crossoverProbability,
    double permutationsPerNode,
    double randomLowerRange,
    double randomUpperRange,
    int numberOfGenerations,
    int testSize
) {
    /**
     * I know it looks horrible, you've got any better idea?
     */
    @Override
    public String toString() {
        return String.format("""
            -- TINY GP (Java version) --
            SEED=%d
            MAX_LEN=%d
            POPSIZE=%d
            DEPTH=%d
            CROSSOVER_PROB=%.3f
            PMUT_PER_NODE=%.3f
            MIN_RANDOM=%.3f
            MAX_RANDOM=%.3f
            GENERATIONS=%d
            TSIZE=%d
            ----------------------------------
            """,
            this.seed, this.maxLength, this.populationSize, this.depth, this.crossoverProbability,
            this.permutationsPerNode, this.randomLowerRange, this.randomUpperRange, this.numberOfGenerations,
            this.testSize);
    }
}
