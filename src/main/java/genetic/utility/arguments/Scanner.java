package genetic.utility.arguments;

import java.io.File;

public class Scanner {
    public Scanner() {

    }

    public TokenType scanInput(String input) {
        if (Scanner.checkForInputFile(input)) return TokenType.InputFile;
        if (Scanner.checkForSeedValue(input)) return TokenType.SeedValue;
        if (Scanner.checkForPrecisionValue(input)) return TokenType.PrecisionValue;

        throw new IllegalArgumentException("Unable to understand this program commandline argument: \"" + input + "\".");
    }

    public static boolean checkForInputFile(String input) {
        File file = new File(input);
        return file.exists();
    }

    public static boolean checkForSeedValue(String input) {
        try {
            Long.parseLong(input);
            return true;
        } catch (NumberFormatException err) {
            return false;
        }
    }

    public static boolean checkForPrecisionValue(String input) {
        try {
            Double.parseDouble(input);
            return true;
        } catch (NumberFormatException err) {
            return false;
        }
    }
}
