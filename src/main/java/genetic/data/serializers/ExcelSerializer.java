package genetic.data.serializers;

import genetic.algorithms.tinygp.fitness.Calculator;
import genetic.algorithms.tinygp.statistics.Statistics;
import genetic.data.Header;
import genetic.data.InputData;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;

public class ExcelSerializer {
    XSSFWorkbook workbook;
    Sheet sheet;
    public ExcelSerializer() {
        this.workbook = new XSSFWorkbook();
        this.sheet = this.workbook.createSheet("Exercise");
    }

    public void write(InputData input, ArrayList<Statistics> history) {
        var index = this.writeHeader(input.header());
        this.writeBody(input.header(), index, input.targets(), convertToIterable(input.targets()), history);
    }

    private int writeHeader(Header header) {
        //  TODO: make it use variables instead of raw values
        Row row = this.sheet.createRow(0);

        row.createCell(0).setCellValue(header.variableNumber());
        row.createCell(1).setCellValue(header.randomConstraintsSize());
        row.createCell(2).setCellValue(header.lowerRange());
        row.createCell(3).setCellValue(header.upperRange());
        row.createCell(4).setCellValue(header.fitnessCases());

        //  Return next available index
        return 1;
    }

    private void writeBody(Header header, int availableIndex, double[][] t, ArrayList<ArrayList<Double>> targets, ArrayList<Statistics> history) {
        final int[] indexes = {availableIndex, 0};

        targets.forEach(row -> {
            var excelRow = this.sheet.createRow(indexes[0]++);
            indexes[1] = 0;
            row.forEach(
                value -> excelRow.createCell(indexes[1]++).setCellValue(value)
            );

            var cell = excelRow.createCell(row.size());

            var calc = new Calculator(header.variableNumber(), t, history.get(history.size() - 1).x());

            var g = new double [row.size()];

            for (int i = 0; i < row.size(); ++i) {
                g[i] = row.get(i);
            }

            cell.setCellValue(calc.calculateTinyGPValue(g, history.get(history.size() - 1).bestProgram()));
        });

        history.forEach(statistics -> {
            var excelRow = this.sheet.createRow(indexes[0]++);

            excelRow.createCell(0).setCellValue(statistics.generationNumber());
            excelRow.createCell(1).setCellValue(statistics.averageFitness());
            excelRow.createCell(2).setCellValue(statistics.bestFitness());
            excelRow.createCell(3).setCellValue(statistics.averageSize());
        });

    }


    private ArrayList<ArrayList<Double>> convertToIterable(double[][] target) {
        ArrayList<ArrayList<Double>> output = new ArrayList<>();

        //  TODO: MAKE BETTER -- it is terrible
        for (double[] doubles : target) {
            ArrayList<Double> list = new ArrayList<>();
            for (double i : doubles)
                list.add(i);
            output.add(list);
        }

        return output;
    }

    public void save(File savePath) throws IOException {
        File parent = savePath.getParentFile();
        if (parent != null && !parent.exists() && !parent.mkdirs())
            throw new IllegalStateException("Couldn't create dir: " + parent);

        FileOutputStream fos = new FileOutputStream(savePath);
        this.workbook.write(fos);
        fos.close();
    }
}
