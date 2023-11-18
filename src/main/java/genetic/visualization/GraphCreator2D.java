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

    private static boolean counter = false;

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
        var chart = ChartFactory.createXYLineChart(
                title,
                xLabel,
                yLabel,
                collection,
                PlotOrientation.VERTICAL,
                true,
                true,
                false
        );

        var plot = chart.getXYPlot();

        if (counter) {
            plot.getRenderer().setSeriesPaint(0, java.awt.Color.RED);
            plot.getRenderer().setSeriesPaint(1, java.awt.Color.BLUE);
        } else {
            plot.getRenderer().setSeriesPaint(0, java.awt.Color.BLUE);
            plot.getRenderer().setSeriesPaint(1, java.awt.Color.RED);
        }

        counter = !counter;

        this.charts.add(
            Pair.of(
                chart,
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
