package genetic.utility.arguments;

import java.io.File;

/**
 * Record that holds the information about program configuration retrieved from program commandline arguments.
 * @param inputFile - Path to input data file.
 * @param seed - Seed to random generator used by genetic algorithms.
 */
public record Config(File inputFile, Long seed) {

    public Config setInputFile(String value) {
        return new Config(new File(value), seed);
    }
    public Config setSeed(String value) {
        return new Config(inputFile, Long.parseLong(value));
    }
}
