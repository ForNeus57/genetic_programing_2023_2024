package genetic.algorithms.tinygp.individual;

import genetic.algorithms.tinygp.TinyGP;

public class IndividualPrinter {
    private final Individual program;
    private final double [] x;
    private final int variableNumber;
    private final StringBuilder builder;

    public IndividualPrinter(Individual program, double [] x, int variableNumber) {
        this.program = program;
        this.x = x;
        this.variableNumber = variableNumber;
        this.builder = new StringBuilder();

        printBody(0);
    }

    public String print() {
        return builder.toString();
    }

    private int printBody(int buffercounter) {
        int a1 = 0, a2;
        //  If we have a variable then ...
        if (this.program.body()[buffercounter] < TinyGP.FSET_START) {
            if (this.program.body()[buffercounter] < this.variableNumber)
                this.builder.append("X").append(this.program.body()[buffercounter] + 1).append(" ");
            else
                this.builder.append(x[this.program.body()[buffercounter]]);
            return ++buffercounter;
        }

        //  If we have an operation in node
        //  We have got a split aka int a1 assigment we check the first part of (<first> <operaton in switch> <second>), and in a2 the second.
        switch (this.program.body()[buffercounter]) {
            case TinyGP.ADD -> {
                this.builder.append("(");
                a1 = printBody(++buffercounter);
                this.builder.append(" + ");
            }
            case TinyGP.SUB -> {
                this.builder.append("(");
                a1 = printBody(++buffercounter);
                this.builder.append(" - ");
            }
            case TinyGP.MUL -> {
                this.builder.append("(");
                a1 = printBody(++buffercounter);
                this.builder.append(" * ");
            }
            case TinyGP.DIV -> {
                this.builder.append("(");
                a1 = printBody(++buffercounter);
                this.builder.append(" / ");
            }
        }
        a2 = printBody(a1);
        this.builder.append( ")");
        return a2;  //  Return where we have left of...
    }
}
