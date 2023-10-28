package genetic.data.deserializers;

import genetic.data.Header;

import java.util.StringTokenizer;

public class HeaderDeserializer {
    private final String line;

    public HeaderDeserializer(String headerLine) {
        this.line = headerLine;
    }

    public Header serialize() {
        var tokens = new StringTokenizer(this.line);

        var varNumber = Integer.parseInt(tokens.nextToken().trim());
        var randomNumber = Integer.parseInt(tokens.nextToken().trim());
        var minRandom =	Double.parseDouble(tokens.nextToken().trim());
        var maxRandom =  Double.parseDouble(tokens.nextToken().trim());
        var fitnessCases = Integer.parseInt(tokens.nextToken().trim());

        return new Header(varNumber, randomNumber, minRandom, maxRandom, fitnessCases);
    }
}
