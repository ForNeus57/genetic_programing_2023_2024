package genetic.data.serializers;

import genetic.data.Header;

import java.util.StringTokenizer;

public class HeaderDataSerializer {
    private final String line;

    private Header header;

    public HeaderDataSerializer(String headerLine) {
        this.line = headerLine;

        this.serialize();
    }

    public Header getHeader() {
        return this.header;
    }

    private void serialize() {
        var tokens = new StringTokenizer(this.line);

        var varNumber = Integer.parseInt(tokens.nextToken().trim());
        var randomNumber = Integer.parseInt(tokens.nextToken().trim());
        var minRandom =	Double.parseDouble(tokens.nextToken().trim());
        var maxRandom =  Double.parseDouble(tokens.nextToken().trim());
        var fitnessCases = Integer.parseInt(tokens.nextToken().trim());

        this.header = new Header(varNumber, randomNumber, minRandom, maxRandom, fitnessCases);
    }
}
