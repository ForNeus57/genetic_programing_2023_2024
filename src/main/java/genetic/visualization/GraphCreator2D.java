package genetic.visualization;

import org.apache.commons.lang3.tuple.Pair;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartUtilities;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class GraphCreator2D {
    private final ArrayList<Pair<JFreeChart, File>> charts;
    public GraphCreator2D() {
        this.charts = new ArrayList<>();
    }
    public void create(ArrayList<Pair<ArrayList<XYSeries>, File>> inputData, String title, String xLabel, String yLabel) {
        inputData.forEach(graph -> this.createGraph(graph.getLeft(), graph.getRight(), title, xLabel, yLabel));
    }

    private void createGraph(ArrayList<XYSeries> inputData, File savePath, String title, String xLabel, String yLabel) {
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
        this.charts.clear();
    }
}
