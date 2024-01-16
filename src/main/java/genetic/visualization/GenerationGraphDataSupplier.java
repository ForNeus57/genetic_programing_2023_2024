package genetic.visualization;

import genetic.algorithms.tinygp.statistics.Statistics;
import org.apache.commons.lang3.tuple.Pair;
import org.jfree.data.xy.XYSeries;

import java.io.File;
import java.util.ArrayList;

public class GenerationGraphDataSupplier {

    private final File savePath;
    private final ArrayList<Statistics> inputData;
    public GenerationGraphDataSupplier(File savePath, ArrayList<Statistics> inputData) {
        this.savePath = savePath;
        this.inputData = inputData;
    }

    public ArrayList<Pair<ArrayList<XYSeries>, File>> convertToXYData() {
        var bestFitnessSeries = new XYSeries("Best fitness");
        var averageFitnessSeries = new XYSeries("Average fitness");

        this.inputData.forEach(statistic -> {
            bestFitnessSeries.add(statistic.generationNumber(), statistic.bestFitness());
            averageFitnessSeries.add(statistic.generationNumber(), statistic.averageFitness());
        });

        return new ArrayList<>() {
            {
                add(Pair.of(
                        new ArrayList<>() {
                            {
                                add(averageFitnessSeries);
                                add(bestFitnessSeries);
                            }
                        },
                        new File(savePath.getAbsolutePath() + "_both.png")
                ));
                add(Pair.of(
                        new ArrayList<>() {
                            {
                                add(bestFitnessSeries);
                            }
                        },
                        new File(savePath.getAbsolutePath() + "_best.png")
                ));
                add(Pair.of(
                        new ArrayList<>() {
                            {
                                add(averageFitnessSeries);
                            }
                        },
                        new File(savePath.getAbsolutePath() + "_average.png")
                ));
            }
        };
    }
}
