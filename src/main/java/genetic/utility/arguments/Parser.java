package genetic.utility.arguments;


import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

/**
 * TODO:    ZIP args and tokens.
 */
public class Parser {
    final ArrayList<String> args;
    ArrayList<TokenType> tokens;

    public Parser(String[] args) {
        this.args = new ArrayList<>(Arrays.stream(args).toList());

        this.getTokens();

        if (!this.checkTokensList())
            throw new IllegalArgumentException("Some commandline arguments were given more than one!");
    }

    public Config parse() {
        //  C style array here, because for some reason in JAVA you cannot capture non-final objects with lambda functions to its scope.
        //  So yes it is a wrapper around it
        //  And yes its evil
        final Config[] output = {new Config(new File("problem.dat"), new Random().nextLong(), -1e-5)};
        final int[] idx = {0};

        this.tokens.forEach(token -> {
            switch (token) {
                //  Extra assigment, because records in JAVA have final fields by default....
                case InputFile -> output[0] = output[0].setInputFile(args.get(idx[0]++));
                case SeedValue -> output[0] = output[0].setSeed(args.get(idx[0]++));
                case PrecisionValue -> output[0] = output[0].setPrecision(args.get(idx[0]++));
            }
        });

        return output[0];
    }

    private void getTokens() {
        this.tokens = new ArrayList<>();
        var scanner = new Scanner();

        this.args.forEach(input -> this.tokens.add(scanner.scanInput(input)));
    }

    /**
     * Method that checks whether the tokens are not repeated for example user provided 2 files path.
     * @return  True if correct, false otherwise.
     */
    private boolean checkTokensList() {
        return this.tokens.stream().distinct().count() == (long) this.tokens.size();
    }
}
