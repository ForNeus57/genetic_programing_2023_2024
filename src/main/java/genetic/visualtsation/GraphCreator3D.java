package genetic.visualtsation;

import genetic.data.ExcelData;
import genetic.data.InputData;

import java.io.File;

public class GraphCreator3D implements GraphCreator {

    private File inputDataWorkbookPath;
    private final InputData inputData;
    private final ExcelData excelInputData;
    public GraphCreator3D(File inputDataWorkbookPath, InputData inputData, ExcelData excelInputData) {
        this.inputDataWorkbookPath = inputDataWorkbookPath;
        this.inputData = inputData;
        this.excelInputData = excelInputData;
    }

    @Override
    public void create() {

    }

    @Override
    public void save() {

    }
}
