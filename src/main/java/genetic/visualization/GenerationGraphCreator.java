package genetic.visualization;

import genetic.algorithms.tinygp.statistics.Statistics;
import org.apache.commons.lang3.tuple.Pair;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartUtilities;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.general.Series;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class GenerationGraphCreator {

    private final File savePath;
    private final ArrayList<Statistics> inputData;
    private final ArrayList<Pair<JFreeChart, File>> charts;
    public GenerationGraphCreator(File savePath, ArrayList<Statistics> inputData) {
        this.savePath = savePath;
        this.inputData = inputData;
        this.charts = new ArrayList<>(3);
    }
    public void create() {
        var data = GenerationGraphCreator.convertToXYData(this.inputData, this.savePath);

        data.forEach(graph -> this.createGraph(graph.getLeft(), "Fitness per generation", "Generation number", "Fitness", graph.getRight()));
    }

    private static ArrayList<Pair<ArrayList<XYSeries>, File>> convertToXYData(ArrayList<Statistics> inputData, File savePath) {
        var bestFitnessSeries = new XYSeries("Best fitness");
        var averageFitnessSeries = new XYSeries("Average fitness");

        inputData.forEach(statistic -> {
            bestFitnessSeries.add(statistic.generationNumber(), statistic.bestFitness());
            averageFitnessSeries.add(statistic.generationNumber(), statistic.averageFitness());
        });

        return new ArrayList<>() {
            {
                add(Pair.of(
                    new ArrayList<>() {
                        {
                            add(bestFitnessSeries);
                            add(averageFitnessSeries);
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

    private void createGraph(ArrayList<XYSeries> inputData, String title, String xLabel, String yLabel, File savePath) {
        var collection = new XYSeriesCollection();
        inputData.forEach(collection::addSeries);
        this.charts.add(
            Pair.of(
                ChartFactory.createXYLineChart(
                    title,
                    xLabel,
                    yLabel,
                    collection,
                    PlotOrientation.VERTICAL,
                    true,
                    true,
                    false
                ),
                savePath
            )
        );
    }

    public void save() {
        this.charts.forEach(chart -> {
            try {
                ChartUtilities.saveChartAsPNG(chart.getRight(), chart.getLeft(), 1000, 600);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
    }
}
