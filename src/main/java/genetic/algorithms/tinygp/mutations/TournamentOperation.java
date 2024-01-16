package genetic.algorithms.tinygp.mutations;

public interface TournamentOperation {
    boolean operation(double fitnessValue, double bestFitnessValue);
}
