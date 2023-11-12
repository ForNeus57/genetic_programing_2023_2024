package genetic.visualtsation;

import genetic.algorithms.tinygp.statistics.Statistics;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartUtilities;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class GenerationGraphCreator implements GraphCreator {

    private final File savePath;
    private final ArrayList<Statistics> inputData;
    private JFreeChart chart;
    public GenerationGraphCreator(File savePath, ArrayList<Statistics> inputData) {
        this.savePath = savePath;
        this.inputData = inputData;
    }
    @Override
    public void create() {
        var bestFitnessSeries = new XYSeries("Best fitness");
        var averageFitnessSeries = new XYSeries("Average fitness");

        for (Statistics statistic : inputData) {
            bestFitnessSeries.add(statistic.generationNumber(), statistic.bestFitness());
            averageFitnessSeries.add(statistic.generationNumber(), statistic.averageFitness());
        }

        var collection = new XYSeriesCollection();
        collection.addSeries(bestFitnessSeries);
        collection.addSeries(averageFitnessSeries);

        this.chart = ChartFactory.createXYLineChart(
            "Best and average fitness per generation",
            "Generation number",
            "Fitness",
            collection,
            PlotOrientation.VERTICAL,
            true,
            true,
            false
        );

    }

    @Override
    public void save() throws IOException {
        ChartUtilities.saveChartAsPNG(this.savePath, chart, 1000, 600);
    }
}
