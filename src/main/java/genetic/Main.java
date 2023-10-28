package genetic;

import genetic.algorithims.TinyGP;
import genetic.utility.arguments.Parser;

public class Main {
    public static void main(String[] args) {
        var parser = new Parser(args);
        var config = parser.parse();
        var gp = new TinyGP(config);
        gp.evolve();
    }
}