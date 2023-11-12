package genetic.algorithims.tinygp;

import genetic.algorithms.tinygp.TinyGP;
import genetic.algorithms.tinygp.orginal.tiny_gp;
import genetic.data.deserializers.InputFileFormatDeserializer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.extension.ExtensionContext;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.ArgumentsProvider;
import org.junit.jupiter.params.provider.ArgumentsSource;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.PrintStream;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.Stream;


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

    static class CartesianProductProvider implements ArgumentsProvider {

        private List<List<String>> generateCartesianProduct(List<List<String>> parameters) {
            List<List<String>> result = List.of(Collections.emptyList());

            for (var paramList : parameters) {
                result = result.stream()
                        .flatMap(list -> paramList.stream().map(item -> {
                            var newList = new java.util.ArrayList<>(list);
                            newList.add(item);
                            return newList;
                        }))
                        .collect(Collectors.toList());
            }

            return result;
        }

        @Override
        public Stream<? extends Arguments> provideArguments(ExtensionContext extensionContext) {
            List<List<String>> parameters = Arrays.asList(
                    this.findInputFiles(),
                    Arrays.asList(
                        "5022820666309059243",
                        "1453486986165295769",
                        "1251194865298280028",
                        "271726382707587018",
                        "6936745913569452631"
                    )
            );

            var cartesianProduct = generateCartesianProduct(parameters);

            return cartesianProduct.stream().map(Arguments::of);
        }

        private List<String> findInputFiles() {
            var inputFiles = new java.util.ArrayList<String>();
            var inputFilesDirectory = new File("src/test/resources/genetic/algorithms/tinygp");
            for (var file : Objects.requireNonNull(inputFilesDirectory.listFiles())) {
                if (file.isFile())
                    inputFiles.add(file.getAbsolutePath());
            }
            return inputFiles;
        }
    }



    @ParameterizedTest
    @ArgumentsSource(CartesianProductProvider.class)
    void checkOutput(List<String> input) {
        long seed = Long.parseLong(input.get(1));

        var inputData = new InputFileFormatDeserializer(new File(input.get(0))).deserialize();

        var modified = new TinyGP(inputData, seed);
        modified.evolve(-1e-5);

        var modified_output = outContent.toString();

        var original = new tiny_gp(input.get(0), seed);
        original.evolve();
        var original_output = outContent.toString();
        original_output = original_output.substring(modified_output.length());

        Assertions.assertEquals(original_output, modified_output);
    }




}