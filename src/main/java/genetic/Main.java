package genetic;

import genetic.algorithms.tinygp.TinyGP;
import genetic.data.deserializers.InputFileFormatDeserializer;
import genetic.data.serializers.ExcelSerializer;
import genetic.utility.arguments.Parser;

import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        var parser = new Parser(args);
        var config = parser.parse();

        var deserializer = new InputFileFormatDeserializer(config.inputFile());
        var inputData = deserializer.deserialize();

        var gp = new TinyGP(inputData, config.seed());
        var history = gp.evolve(-1e-5);


        //  Excel...
        try {
            var excelWriter = new ExcelSerializer();
            excelWriter.write(inputData, history);
            excelWriter.save(new File("./data/generated/excel/problem.xlsx"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}