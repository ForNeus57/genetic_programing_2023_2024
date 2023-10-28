package genetic.data;

/**
 * Representation of input data file header.
 *
 * @param variableNumber - Number of X variable the program uses: X1, X2, X3 for 3 ...
 * @param randomConstraintsSize - The number of random constraints.
 * @param lowerRange - The minimum value of the random constraints.
 * @param upperRange - The maximum value of the random constraints.
 * @param fitnessCases - Number of fitness cases - how many different key-value pairs (x, f(x)) there are in a program. AKA the number of lines with values - 1. No clue why to include it, but ok - it can be counted on the fly by BufferReader(new FileReader(...)).
 */
public record Header(int variableNumber, int randomConstraintsSize, double lowerRange, double upperRange, int fitnessCases) {

}
