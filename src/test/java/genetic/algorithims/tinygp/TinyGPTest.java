package genetic.algorithims.tinygp;

import genetic.algorithms.tinygp.TinyGP;
import genetic.algorithms.tinygp.orginal.tiny_gp;
import genetic.data.deserializers.InputFileFormatDeserializer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;


/**
 * TODO: MAKE THIS BETTER
 */
class TinyGPTest {

    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final ByteArrayOutputStream errContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;
    private final PrintStream originalErr = System.err;

    @BeforeEach
    void setUp() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @AfterEach
    void tearDown() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }

    @ParameterizedTest
    @ValueSource(strings = {"5022820666309059243", "1453486986165295769", "1251194865298280028", "271726382707587018", "6936745913569452631", "122663306635557294"})
    void checkOutput1(String seedInput) {
        long seed = Long.parseLong(seedInput);
        var file = "src/test/resources/xmxp2.dat";

        var inputData = new InputFileFormatDeserializer(new File(file)).deserialize();

        var modified = new TinyGP(inputData, seed);
        modified.evolve(-1e-5);

        var modified_output = outContent.toString();

        var original = new tiny_gp(file, seed);
        original.evolve();
        var original_output = outContent.toString();
        original_output = original_output.substring(modified_output.length());

        Assertions.assertEquals(original_output, modified_output);
    }

}