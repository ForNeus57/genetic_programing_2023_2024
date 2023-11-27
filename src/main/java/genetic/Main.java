package genetic;

import genetic.algorithms.tinygp.TinyGP;
import genetic.algorithms.tinygp.fitness.Calculator;
import genetic.data.ExcelData;
import genetic.data.deserializers.InputFileFormatDeserializer;
import genetic.data.serializers.ExcelSerializer;
import genetic.utility.arguments.Parser;
import genetic.visualization.Function2DGraphDataSupplier;
import genetic.visualization.GenerationGraphDataSupplier;
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

        try {
            //  Create logs.
            var logPath = new File(config.inputFile().getParent() + "/generated/logs/" + config.inputFile().getName().split("\\.")[0] + "_new.txt");
            var logFile = new File(logPath.getAbsolutePath());
            var output = gp.output.toString();

            logFile.createNewFile();
            var writer = new java.io.FileWriter(logFile);
            writer.write(output);
            writer.close();

            //  Excel....
            var savePath = new File(config.inputFile().getParent() + "/generated/excel/" + config.inputFile().getName().split("\\.")[0] + "_new.xlsx");
            var resultsImagePath = new File(config.inputFile().getParent() + "/generated/images/" + config.inputFile().getName().split("\\.")[0] + "_new_results");
            var generationsImagePath = new File(config.inputFile().getParent() + "/generated/images/" + config.inputFile().getName().split("\\.")[0] + "_new_generations");

            var excelWriter = new ExcelSerializer();
            excelWriter.write(inputData, history);
            excelWriter.save(savePath);


            var calc = new Calculator(inputData.header().variableNumber(), inputData.targets(), history.get(history.size() - 1).x());
            var excelTinyGPOutput = new ArrayList<Double>();

            for (var target : inputData.targets()) {
                excelTinyGPOutput.add(calc.calculateTinyGPValue(target, history.get(history.size() - 1).bestProgram()));
            }

            var excelData = new ExcelData(excelTinyGPOutput);

            var creator = new GraphCreator2D();

            if (inputData.header().variableNumber() > 1) {
                var creator3D = new GraphCreator3D(
                    new File(config.inputFile().getParent() + "/generated/images/" + config.inputFile().getName().split("\\.")[0] + "_new_results"),
                    inputData,
                    excelData);
                creator3D.create();
            } else {
                var converter = new Function2DGraphDataSupplier(resultsImagePath, inputData, excelData);
                creator.create(converter.convertToXYData(), "TinyGP vs f(x) = y", "X", "Y");
                creator.save();
            }

            var converter = new GenerationGraphDataSupplier(generationsImagePath, history);
            creator.create(converter.convertToXYData(), "TinyGP generations", "Generation", "Fitness");
            creator.save();

            //  Temporary fix to close program after screenshot.
            System.exit(0);
        } catch (Exception err) {
            throw new RuntimeException(err);
        }
    }
}