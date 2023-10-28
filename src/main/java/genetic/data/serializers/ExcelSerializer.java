package genetic.data.serializers;

import genetic.data.Header;
import genetic.data.InputData;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class ExcelSerializer {
    XSSFWorkbook workbook;
    Sheet sheet;
    public ExcelSerializer() {
        this.workbook = new XSSFWorkbook();
        this.sheet = this.workbook.createSheet("Exercise");
    }

    public void write(InputData input) throws IOException {
        var index = this.writeHeader(input.header());
        this.writeBody(index, convertToIterable(input.header(), input.targets()));
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

    private void writeBody(int availableIndex, ArrayList<ArrayList<Double>> targets) {
        final int[] indexes = {0, 0};

        targets.forEach(row -> {
            Row excelRow = this.sheet.createRow(indexes[0]++);
            indexes[1] = 0;
            row.forEach(
                value -> excelRow.createCell(indexes[1]++).setCellValue(value)
            );
        });
    }

    private ArrayList<ArrayList<Double>> convertToIterable(Header header, double[][] target) {
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
