package genetic.algorithms.tinygp.individual;


import genetic.algorithms.tinygp.TinyGP;

import static genetic.algorithms.tinygp.TinyGP.FSET_START;

public class Individual {
    private final char [] body;
    private int size;
    public Individual(char[] body) {
        this.body = body;
        this.size = 0;
    }

    public int size() {
        this.size = 0;
        this.size = this.getSizeByTraversing(this.size);
        return this.size;
    }

    public int size(int point) {
        this.size = point;
        this.size = this.getSizeByTraversing(this.size);
        return this.size;
    }

    private int getSizeByTraversing(int traversingSize) {
        if (this.body[traversingSize] < FSET_START)
            return ++traversingSize;

        switch(this.body[traversingSize]) {
            case TinyGP.ADD:
            case TinyGP.SUB:
            case TinyGP.MUL:
            case TinyGP.DIV:
                return this.getSizeByTraversing(this.getSizeByTraversing(++traversingSize));
            case TinyGP.SIN:
            case TinyGP.COS:
                return this.getSizeByTraversing(++traversingSize);
        }

        throw new IndexOutOfBoundsException("Unknown operation");
    }

    public char[] body() {
        return this.body;
    }
}
