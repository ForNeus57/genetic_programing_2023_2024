from src.genetic.interpreter.input_output import BufferInputOutputOperation
from src.genetic.interpreter.interpreter import Interpreter


def test_write_unknown():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write(x);
    }
    """, BufferInputOutputOperation((1,)))
    assert output.output == [1]


def test_write_int():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write(1);
    }
    """, BufferInputOutputOperation())
    assert output.output == [1]


def test_write_expression():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write(((7 + 4) / 3));
    }
    """, BufferInputOutputOperation())
    assert output.output == [3]


def test_read_unknown():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        read(x);
        x = (x + 1);
        write(x);
    }
    """, BufferInputOutputOperation((1,)))
    assert output.output == [2]


def test_read_int():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        x = -3;
        read(x);
        write(x);
    }
    """, BufferInputOutputOperation((17,)))
    assert output.output == [17]


def test_operation_add():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 + 11));
    }
    """, BufferInputOutputOperation())
    assert output.output == [18]


def test_operation_subtract():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 - 11));
    }
    """, BufferInputOutputOperation())
    assert output.output == [-4]


def test_operation_multiply():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 * -11));
    }
    """, BufferInputOutputOperation())
    assert output.output == [-77]


def test_operation_divide():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 / -11));
    }
    """, BufferInputOutputOperation())
    assert output.output == [-1]


def test_operation_divide_by_zero():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 / 0));
    }
    """, BufferInputOutputOperation())
    assert output.output == [7]


def test_operation_negation_false():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if (!(false)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [1]


def test_operation_negation_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if (!(true)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [0]


def test_operation_less_then_false():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 < 0)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [0]


def test_operation_less_then_false_equal():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 < 7)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [0]


def test_operation_less_then_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 < 10)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [1]


def test_operation_less_equal_then_false():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 <= 0)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [0]


def test_operation_less_equal_then_false_equal():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 <= 7)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [1]


def test_operation_less_equal_then_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 <= 10)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [1]


def test_operation_grater_then_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 > 0)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [1]


def test_operation_grater_then_false_equal():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 > 7)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [0]


def test_operation_grater_then_false():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 > 10)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [0]


def test_operation_grater_equal_then_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 >= 0)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [1]


def test_operation_grater_equal_then_false_equal():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 >= 7)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [1]


def test_operation_grater_equal_then_false():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if ((7 >= 10)) {
            write(1);
        } else {
            write(0);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [0]


def test_assigment_unknown():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        x = (x + 1);
        write(x);
    }
    """, BufferInputOutputOperation((-2, )))
    assert output.output == [-1]


def test_if_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if (true) {
            write(15);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [15]


def test_if_false():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if (false) {
            write(15);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == []


def test_if_true_else():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if (true) {
            write(15);
        } else {
            write(-111);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [15]


def test_if_false_else():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        if (false) {
            write(15);
        } else {
            write(-111);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [-111]


def test_loop_infinite():
    Interpreter.interpret("""
    {
        while (true) {
            write(15);
        }
    }
    """, BufferInputOutputOperation())


def test_loop_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        i = 0;
        while ((i < 5)) {
            write(i);
            i = (i + 1);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == [0, 1, 2, 3, 4]


def test_loop_false():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        while (false) {
            write(15);
        }
    }
    """, BufferInputOutputOperation())
    assert output.output == []
