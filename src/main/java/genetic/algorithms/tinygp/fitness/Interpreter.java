package genetic.algorithms.tinygp.fitness;


import genetic.algorithms.tinygp.individual.Individual;
import genetic.algorithms.tinygp.TinyGP;

public class Interpreter {
    private final Individual program;      //  The program is the values ie the String (1231.1 * X1) + 1.234 ....
    private final double [] x;          //  Still no clue what it is...
    private int currentPosition;

    public Interpreter(Individual program, double[] x) {
        this.program = program;
        this.x = x;
        this.currentPosition = 0;
    }

    public double run() {
        char primitive = this.program.body()[this.currentPosition++];   //  It is stupid to use char as index for nodes positions and also as a token type.
        if (primitive < TinyGP.FSET_START)     //  If a node is not an operation then return its value like 2.123314 ... I guess?
            return(x[primitive]);

        return handleOperation(primitive);
    }

    private double handleOperation(char primitive) {
        switch (primitive) {
            case TinyGP.ADD -> {
                return run() + run();
            }
            case TinyGP.SUB -> {
                return run() - run();
            }
            case TinyGP.MUL -> {
                return run() * run();
            }
            case TinyGP.DIV -> {
                double num = run(), den = run();
                if (Math.abs(den) <= 0.001)
                    return num;
                else
                    return num / den;
            }
        }
        return 0.0;     //  Should never execute
    }
}
