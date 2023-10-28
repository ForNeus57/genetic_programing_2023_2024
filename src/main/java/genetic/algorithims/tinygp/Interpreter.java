package genetic.algorithims.tinygp;


import static genetic.algorithims.tinygp.TinyGP.*;

public class Interpreter {
    private final char [] program;
    private final double [] x;
    private int pc;     //  Change later to better name

    Interpreter(char[] program, double[] x) {
        this.program = program;
        this.x = x;
        this.pc = 0;
    }

    public double run() {
        char primitive = this.program[this.pc++];
        if ( primitive < FSET_START )       //  Max array length for given
            return(x[primitive]);
        switch (primitive) {
            case ADD -> {
                return (run() + run());
            }
            case SUB -> {
                return (run() - run());
            }
            case MUL -> {
                return (run() * run());
            }
            case DIV -> {
                double num = run(), den = run();
                if (Math.abs(den) <= 0.001)
                    return (num);
                else
                    return (num / den);
            }
        }
        return 0.0;
    }
}
