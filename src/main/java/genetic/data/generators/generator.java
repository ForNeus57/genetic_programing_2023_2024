package genetic.data.generators;

import genetic.data.functions.function;

import java.util.ArrayList;
import java.util.List;

public class generator {
    private final function func;
    private final domain range;

    public generator(function func, domain range) {
        this.func = func;
        this.range = range;
    }

    /**
     * Make it to be in range class
     * @return
     */
    public List<Double> seed() {
        return new ArrayList<>();
    }

    public List<Double> generate(List<Double> x) {
        return new ArrayList<>();
    }
}
