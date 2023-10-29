package genetic.algorithms.tinygp.statistics;

import static java.lang.String.format;

public record Statistics(
    int generationNumber,
    double averageFitness,
    double bestFitness,
    double averageSize,
    String bestIndividual
) {
    @Override
    public String toString() {
        return String.format(
            """
            Generation=%d Avg Fitness=%.10f Best Fitness=%.10f Avg Size=%.10f
            Best Individual: %s
            """,
            this.generationNumber, this.averageFitness, this.bestFitness, this.averageSize, this.bestIndividual
        );
    }
}
