package genetic.algorithims.tinygp;

import genetic.algorithims.tinygp.orginal.tiny_gp;
import genetic.data.deserializers.InputFileFormatDeserializer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.*;

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

    @Test
    void checkOutput1() {
        long seed = Long.parseLong("5022820666309059243");
        var file = "src/test/resources/xmxp2.dat";

        var inputData = new InputFileFormatDeserializer(new File(file)).deserialize();

        var modified = new TinyGP(inputData, seed);
        if (modified.evolve(-1e-5))
            System.out.print("PROBLEM SOLVED\n");
        else
            System.out.print("PROBLEM *NOT* SOLVED\n");

        var modified_output = outContent.toString();

        var original = new tiny_gp(file, seed);
        original.evolve();
        var original_output = outContent.toString();
        original_output = original_output.substring(modified_output.length());

        assertEquals(original_output, modified_output);
    }

    @Test
    void checkOutput2() {
        long seed = Long.parseLong("1453486986165295769");
        var file = "src/test/resources/xmxp2.dat";

        var inputData = new InputFileFormatDeserializer(new File(file)).deserialize();

        var modified = new TinyGP(inputData, seed);
        if (modified.evolve(-1e-5))
            System.out.print("PROBLEM SOLVED\n");
        else
            System.out.print("PROBLEM *NOT* SOLVED\n");

        var modified_output = outContent.toString();

        var original = new tiny_gp(file, seed);
        original.evolve();
        var original_output = outContent.toString();
        original_output = original_output.substring(modified_output.length());

        assertEquals(original_output, modified_output);
    }

    @Test
    void checkOutput3() {
        long seed = Long.parseLong("1251194865298280028");
        var file = "src/test/resources/xmxp2.dat";

        var inputData = new InputFileFormatDeserializer(new File(file)).deserialize();

        var modified = new TinyGP(inputData, seed);
        if (modified.evolve(-1e-5))
            System.out.print("PROBLEM SOLVED\n");
        else
            System.out.print("PROBLEM *NOT* SOLVED\n");

        var modified_output = outContent.toString();

        var original = new tiny_gp(file, seed);
        original.evolve();
        var original_output = outContent.toString();
        original_output = original_output.substring(modified_output.length());

        assertEquals(original_output, modified_output);
    }

    @Test
    void checkOutput4() {
        long seed = Long.parseLong("271726382707587018");
        var file = "src/test/resources/xmxp2.dat";

        var inputData = new InputFileFormatDeserializer(new File(file)).deserialize();

        var modified = new TinyGP(inputData, seed);
        if (modified.evolve(-1e-5))
            System.out.print("PROBLEM SOLVED\n");
        else
            System.out.print("PROBLEM *NOT* SOLVED\n");

        var modified_output = outContent.toString();

        var original = new tiny_gp(file, seed);
        original.evolve();
        var original_output = outContent.toString();
        original_output = original_output.substring(modified_output.length());

        assertEquals(original_output, modified_output);
    }

    @Test
    void checkOutput5() {
        long seed = Long.parseLong("6936745913569452631");
        var file = "src/test/resources/xmxp2.dat";

        var inputData = new InputFileFormatDeserializer(new File(file)).deserialize();

        var modified = new TinyGP(inputData, seed);
        if (modified.evolve(-1e-5))
            System.out.print("PROBLEM SOLVED\n");
        else
            System.out.print("PROBLEM *NOT* SOLVED\n");

        var modified_output = outContent.toString();

        var original = new tiny_gp(file, seed);
        original.evolve();
        var original_output = outContent.toString();
        original_output = original_output.substring(modified_output.length());

        assertEquals(original_output, modified_output);
    }

    @Test
    void checkOutput6() {
        long seed = Long.parseLong("122663306635557294");
        var file = "src/test/resources/xmxp2.dat";

        var inputData = new InputFileFormatDeserializer(new File(file)).deserialize();

        var modified = new TinyGP(inputData, seed);
        if (modified.evolve(-1e-5))
            System.out.print("PROBLEM SOLVED\n");
        else
            System.out.print("PROBLEM *NOT* SOLVED\n");

        var modified_output = outContent.toString();

        var original = new tiny_gp(file, seed);
        original.evolve();
        var original_output = outContent.toString();
        original_output = original_output.substring(modified_output.length());

        assertEquals(original_output, modified_output);
    }


}