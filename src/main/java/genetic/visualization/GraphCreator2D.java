package genetic.visualization;

import genetic.data.ExcelData;
import genetic.data.InputData;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartUtilities;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.io.File;
import java.io.IOException;

public class GraphCreator2D implements GraphCreator {

    private final File savePath;
    private final InputData inputData;
    private final ExcelData excelInputData;

    private JFreeChart chart;
    public GraphCreator2D(File savePath, InputData inputData, ExcelData excelInputData) {
        this.savePath = savePath;
        this.inputData = inputData;
        this.excelInputData = excelInputData;
    }

    @Override
    public void create() {
        var functionSeries = new XYSeries("y = f(x)");
        var tinyGPSeries = new XYSeries("TinyGP(x)");

        for (int i = 0; i < excelInputData.calculatedValues().size(); ++i) {
            functionSeries.add(inputData.targets()[i][0], inputData.targets()[i][1]);
            tinyGPSeries.add(inputData.targets()[i][0], excelInputData.calculatedValues().get(i));
        }

        var collection = new XYSeriesCollection();
        collection.addSeries(functionSeries);
        collection.addSeries(tinyGPSeries);

        this.chart = ChartFactory.createXYLineChart(
                "TinyGP vs function y = f(x)",
                "X",
                "Y",
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
