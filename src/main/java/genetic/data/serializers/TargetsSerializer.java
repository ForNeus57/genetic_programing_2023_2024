package genetic.data.serializers;

import genetic.data.Header;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;


public class TargetsSerializer {

    private final Header header;
    private final BufferedReader dataFile;

    public TargetsSerializer(Header header, BufferedReader dataFile) {
        this.header = header;
        this.dataFile = dataFile;
    }

    public double[][] serialize() throws IOException {
        //  + 1 at the end because we also need to store the f(x)
        //  TODO: Make ArrayList<ArrayList<Double>>....
        var output = new double[this.header.fitnessCases()][this.header.variableNumber() + 1];

        for (int i = 0; i < this.header.fitnessCases(); i++) {
            var line = this.dataFile.readLine();
            var tokens = new StringTokenizer(line);
            for (int j = 0; j <= this.header.variableNumber(); j++)
                output[i][j] = Double.parseDouble(tokens.nextToken().trim());
        }
        return output;
    }
}
