package genetic.algorithims.tinygp.fitness;


import static genetic.algorithims.tinygp.TinyGP.*;  //  Remove this and make some sens with ADD, FSET_START and so on

public class Interpreter {
    private final char [] program;      //  The program is the values ie the String (1231.1 * X1) + 1.234 ....
    private final double [] x;          //  Still no clue what it is...
    private int currentPosition;

    public Interpreter(char[] program, double[] x) {
        this.program = program;
        this.x = x;
        this.currentPosition = 0;
    }

    public double run() {
        char primitive = this.program[this.currentPosition++];   //  It is stupid to use char as index for nodes positions and also as a token type.
        if (primitive < FSET_START)     //  If a node is not an operation then return its value like 2.123314 ... I guess?
            return(x[primitive]);

        return handleOperation(primitive);
    }

    private double handleOperation(char primitive) {
        switch (primitive) {
            case ADD -> {
                return run() + run();
            }
            case SUB -> {
                return run() - run();
            }
            case MUL -> {
                return run() * run();
            }
            case DIV -> {
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
