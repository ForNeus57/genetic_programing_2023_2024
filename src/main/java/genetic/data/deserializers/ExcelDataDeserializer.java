package genetic.data.deserializers;

import genetic.data.ExcelData;
import org.apache.poi.openxml4j.exceptions.InvalidFormatException;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class ExcelDataDeserializer {

    private final File inputPath;

    public ExcelDataDeserializer(File inputPath) {
        this.inputPath = inputPath;
    }

    public ExcelData deserialize() throws IOException, InvalidFormatException {
        var workbook = new XSSFWorkbook(inputPath);
        var sheet = workbook.getSheetAt(0);

        var iter = sheet.iterator();
        var header = iter.next();
        var variableNumber = (int) header.getCell(0).getNumericCellValue();
        var randomNumber = (int) header.getCell(1).getNumericCellValue();
        ArrayList<Double> output = new ArrayList<>();
        for (int i = 0; i < randomNumber; ++i) {
            output.add(iter.next().getCell(variableNumber + 1).getNumericCellValue());
        }

        return new ExcelData(output);
    }

}
