package genetic;

import genetic.algorithms.tinygp.TinyGP;
import genetic.data.deserializers.ExcelDataDeserializer;
import genetic.data.deserializers.InputFileFormatDeserializer;
import genetic.data.serializers.ExcelSerializer;
import genetic.utility.arguments.Parser;
import genetic.visualization.GenerationGraphCreator;
import genetic.visualization.GraphCreator;
import genetic.visualization.GraphCreator2D;
import genetic.visualization.GraphCreator3D;

import java.io.File;

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
            var savePath = new File(config.inputFile().getParent() + "/generated/excel/" + config.inputFile().getName().split("\\.")[0] + ".xlsx");
            var resultsImagePath = new File(config.inputFile().getParent() + "/generated/images/" + config.inputFile().getName().split("\\.")[0] + "_results.png");
            var generationsImagePath = new File(config.inputFile().getParent() + "/generated/images/" + config.inputFile().getName().split("\\.")[0] + "_generations.png");

            var excelWriter = new ExcelSerializer();
            excelWriter.write(inputData, history);
            excelWriter.save(savePath);

            var excelDeserializer = new ExcelDataDeserializer(savePath);
            var excelData = excelDeserializer.deserialize();

            GraphCreator creator = null;
            if (inputData.header().variableNumber() > 1) {
                creator = new GraphCreator3D(resultsImagePath, inputData, excelData);
            } else {
                creator = new GraphCreator2D(resultsImagePath, inputData, excelData);
            }

            creator.create();
            creator.save();

            creator = new GenerationGraphCreator(generationsImagePath, history);

            creator.create();
            creator.save();

            //  Temporary fix to close program after screenshot.
//            System.exit(0);
        } catch (Exception err) {
            throw new RuntimeException(err);
        }
    }
}