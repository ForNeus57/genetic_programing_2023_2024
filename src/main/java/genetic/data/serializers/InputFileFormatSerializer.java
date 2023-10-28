package genetic.data.serializers;

import genetic.data.Header;
import genetic.data.InputData;

import java.io.*;
import java.util.ArrayList;


/**
 *
 * No clue why this input file is not a binary file, it would have saved space and improved runtime...
 * I guess it is more visible that way.
 */
public class InputFileFormatSerializer {

    //  Cannot make final, because it marks red due to there being a possibility that program will execute code after the catch block if exception found... Stupid JAVA
    private InputData data;

    public InputFileFormatSerializer(File input) {
        try {
            BufferedReader in = new BufferedReader(new FileReader(input));

            var header = parseHeader(in.readLine());
            this.data = new InputData(header, parseData(header, in));

            in.close();
        } catch (FileNotFoundException e) {
            System.out.println("ERROR: Please provide a data file");
            System.exit(0);
        } catch(Exception e) {
            System.out.println("ERROR: Incorrect data format");
            System.exit(0);
        }
    }

    public InputData serialize() {
        return data;
    }

    private Header parseHeader(String headerLine) {
        var serializer = new HeaderSerializer(headerLine);
        return serializer.serialize();
    }

    private double[][] parseData(Header header, BufferedReader inputFile) throws IOException {
        var serializer = new TargetsSerializer(header, inputFile);
        return serializer.serialize();
    }

}
