package genetic.visualization;

import genetic.data.ExcelData;
import genetic.data.InputData;
import org.apache.commons.lang3.tuple.Pair;
import org.jfree.data.xy.XYSeries;

import java.io.File;
import java.util.ArrayList;

public class Function2DGraphDataSupplier {
    private final File savePath;
    private final InputData inputData;
    private final ExcelData excelInputData;

    public Function2DGraphDataSupplier(File savePath, InputData inputData, ExcelData excelInputData) {
        this.savePath = savePath;
        this.inputData = inputData;
        this.excelInputData = excelInputData;
    }

    public ArrayList<Pair<ArrayList<XYSeries>, File>> convertToXYData() {
        var functionSeries = new XYSeries("y = f(x)");
        var tinyGPSeries = new XYSeries("TinyGP(x)");

        for (int i = 0; i < excelInputData.calculatedValues().size(); ++i) {
            functionSeries.add(inputData.targets()[i][0], inputData.targets()[i][1]);
            tinyGPSeries.add(inputData.targets()[i][0], excelInputData.calculatedValues().get(i));
        }

        return new ArrayList<>() {
            {
                add(Pair.of(
                        new ArrayList<>() {
                            {
                                add(tinyGPSeries);
                                add(functionSeries);
                            }
                        },
                        new File(savePath.getAbsolutePath() + "_both.png")
                ));
                add(Pair.of(
                        new ArrayList<>() {
                            {
                                add(functionSeries);
                            }
                        },
                        new File(savePath.getAbsolutePath() + "_function.png")
                ));
                add(Pair.of(
                        new ArrayList<>() {
                            {
                                add(tinyGPSeries);
                            }
                        },
                        new File(savePath.getAbsolutePath() + "_tiny_gp.png")
                ));
            }
        };
    }
}
