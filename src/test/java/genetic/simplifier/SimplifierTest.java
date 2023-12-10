package genetic.simplifier;

import genetic.Simplifier;
import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.TestFactory;
import java.util.Arrays;
import java.util.Collection;
import static org.junit.jupiter.api.Assertions.assertEquals;

class SimplifierTest {

    @TestFactory
    Collection<DynamicTest> testSimplify() {
        return Arrays.asList(
                dynamicTest("Example 1",
                            "((X1 * (3.2 + 3.4)) * 2)",
                            "((X1 * 6.6) * 2)"),
                dynamicTest("Example 2",
                            "(X1 * (((3.2 + 3.4) / (3.3 + 3.3)) * 2))",
                            "(X1 * 2.0)"),
                dynamicTest("No Change",
                            "((X1 * 2) + (X2 / 3))",
                            "((X1 * 2) + (X2 / 3))"),
                dynamicTest("Nested Expressions",
                            "(((X1 * 2) + 3) * ((X2 / 2) - 1))",
                            "(((X1 * 2) + 3) * ((X2 / 2) - 1))"),
                dynamicTest("Single Value",
                            "(3.14)",
                            "(3.14)"),
                dynamicTest("Single Value 2",
                            "((3.14 + 2))",
                            "(5.140000000000001)"),
                dynamicTest("Single Value 3",
                            "((3.14 - 2))",
                            "(1.1400000000000001)"),
                dynamicTest("Single Value 4",
                            "((3.14 * 2))",
                            "(6.28)"),
                dynamicTest("Single Value 5",
                            "((3.14 / 2))",
                            "(1.57)"),
                dynamicTest("Cos and sin",
                            "((X1 * sin(0.5)) + (cos(X2) / 3)))",
                            "((X1 * sin(0.5)) + (cos(X2) / 3))")
        );
    }

    private DynamicTest dynamicTest(String testName, String oldProgram, String expectedSimplifiedProgram) {
        return DynamicTest.dynamicTest(testName, () -> {
            Simplifier s = new Simplifier();
            String newProgram = s.simplify(oldProgram);
            assertEquals(expectedSimplifiedProgram, newProgram);
        });
    }
}