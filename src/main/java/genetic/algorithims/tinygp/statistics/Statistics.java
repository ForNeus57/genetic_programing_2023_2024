package genetic.algorithims.tinygp.statistics;

public record Statistics(
    int generationNumber,
    double averageFitness,
    double bestFitness,
    double averageSize,
    String bestIndividual
) {

}
