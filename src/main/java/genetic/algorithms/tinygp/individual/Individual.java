package genetic.algorithms.tinygp.individual;


public class Individual {
    private final char [] body;
    private int size;
    public Individual(char[] body) {
        this.body = body;
        this.size = 0;
    }

    //  DOES NOT WORK
//    public int size() {
//        this.size = 0;
//        return this.getSizeByTraversing();
//    }
//
//    private int getSizeByTraversing() {
//        if (this.body[this.size] < FSET_START)
//            return ++this.size;
//
//        ++this.size;
//        return this.getSizeByTraversing();
//    }

    public char[] body() {
        return this.body;
    }
}
