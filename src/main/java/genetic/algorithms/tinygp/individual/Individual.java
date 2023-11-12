package genetic.algorithms.tinygp.individual;


import static genetic.algorithms.tinygp.TinyGP.FSET_START;

public class Individual {
    private final char [] body;
    private int size;
    public Individual(char[] body) {
        this.body = body;
        this.size = 0;
    }

    //  DOES NOT WORK
    public int size() {
        this.size = 0;
        this.size = this.getSizeByTraversing(this.size);
        return this.size;
    }

    private int getSizeByTraversing(int traversingSize) {
        if (this.body[traversingSize] < FSET_START)
            return ++traversingSize;

        return this.getSizeByTraversing(this.getSizeByTraversing(++traversingSize));
    }

    public char[] body() {
        return this.body;
    }
}
