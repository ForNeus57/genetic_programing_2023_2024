package genetic;

import genetic.algorithims.tinygp.TinyGP;
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
        if (gp.evolve(-1e-5))
            System.out.println("PROBLEM SOLVED");
        else
            System.out.println("PROBLEM *NOT* SOLVED");


        //  Excel...
        try {
            var excelWriter = new ExcelSerializer();
            excelWriter.write(inputData);
            excelWriter.save(new File("./data/generated/excel/problem.xlsx"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}