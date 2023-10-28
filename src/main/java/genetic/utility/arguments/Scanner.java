package genetic.utility.arguments;

import java.io.File;

public class Scanner {
    public Scanner() {

    }

    public TokenType scanInput(String input) {
        if (checkForInputFile(input)) return TokenType.InputFile;
        if (checkForSeedValue(input)) return TokenType.SeedValue;

        throw new IllegalArgumentException("Unable to understand this program commandline argument: \"" + input + "\".");
    }

    public boolean checkForInputFile(String input) {
        File file = new File(input);
        return file.exists();
    }

    public boolean checkForSeedValue(String input) {
        try {
            Long.parseLong(input);
            return true;
        } catch (NumberFormatException err) {
            return false;
        }
    }
}
