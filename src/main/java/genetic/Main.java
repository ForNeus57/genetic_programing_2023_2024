package genetic;

import genetic.algorithms.tinygp.TinyGP;
import genetic.algorithms.tinygp.fitness.Calculator;
import genetic.data.ExcelData;
import genetic.data.deserializers.InputFileFormatDeserializer;
import genetic.data.serializers.ExcelSerializer;
import genetic.utility.arguments.Parser;
import genetic.visualization.GenerationGraphCreator;
import genetic.visualization.GraphCreator2D;
import genetic.visualization.GraphCreator3D;

import java.io.File;
import java.util.ArrayList;

public class Main {



    public static void main(String[] args) {
        var parser = new Parser(args);
        var config = parser.parse();

        var deserializer = new InputFileFormatDeserializer(config.inputFile());
        var inputData = deserializer.deserialize();

        var gp = new TinyGP(inputData, config.seed());
        var history = gp.evolve(config.precision());

        //  Excel...
        try {
            var savePath = new File(config.inputFile().getParent() + "/generated/excel/" + config.inputFile().getName().split("\\.")[0] + ".xlsx");
            var resultsImagePath = new File(config.inputFile().getParent() + "/generated/images/" + config.inputFile().getName().split("\\.")[0] + "_results.png");
            var generationsImagePath = new File(config.inputFile().getParent() + "/generated/images/" + config.inputFile().getName().split("\\.")[0] + "_generations.png");

            var excelWriter = new ExcelSerializer();
            excelWriter.write(inputData, history);
            excelWriter.save(savePath);


            var calc = new Calculator(inputData.header().variableNumber(), inputData.targets(), history.get(history.size() - 1).x());
            var excelTinyGPOutput = new ArrayList<Double>();

            for (var target : inputData.targets()) {
                excelTinyGPOutput.add(calc.calculateTinyGPValue(target, history.get(history.size() - 1).bestProgram()));
            }

            var excelData = new ExcelData(excelTinyGPOutput);

            if (inputData.header().variableNumber() > 1) {
                var creator = new GraphCreator3D(
                        new File(config.inputFile().getParent() + "/generated/images/" + config.inputFile().getName().split("\\.")[0] + "_results"),
                        inputData, excelData);
                creator.create();
            } else {
                var creator = new GraphCreator2D(resultsImagePath, inputData, excelData);
                creator.create();
                creator.save();
            }

            var creator = new GenerationGraphCreator(generationsImagePath, history);
            creator.create();
            creator.save();

            //  Temporary fix to close program after screenshot.
            System.exit(0);
        } catch (Exception err) {
            throw new RuntimeException(err);
        }
    }
}