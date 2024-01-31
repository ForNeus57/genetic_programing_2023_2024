from src.genetic.interpreter.input_output import BufferInputOutputOperation
from src.genetic.interpreter.interpreter import Interpreter


def test_write_unknown():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write(x);
    }
    """, BufferInputOutputOperation([1]))
    assert output.output == [1]


def test_write_int():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write(1);
    }
    """, BufferInputOutputOperation())
    assert output.output == [1]


def test_write_bool():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write(true);
    }
    """, BufferInputOutputOperation())
    assert output.output == [True]


def test_write_expression():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write(((7 + 4) / 3));
    }
    """, BufferInputOutputOperation())
    assert output.output == [3]


def test_write_condition():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write(((7 + 4) == 4));
    }
    """, BufferInputOutputOperation())
    assert output.output == [False]


def test_read_unknown():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        read(x);
        x = (x + 1);
        write(x);
    }
    """, BufferInputOutputOperation([1]))
    assert output.output == [2]


def test_read_int():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        int x = -3;
        read(x);
        write(x);
    }
    """, BufferInputOutputOperation([17]))
    assert output.output == [17]


def test_read_bool():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        bool x = false;
        read(x);
        write(x);
    }
    """, BufferInputOutputOperation([True]))
    assert output.output == [True]


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
        write(!(false));
    }
    """, BufferInputOutputOperation())
    assert output.output == [True]


def test_operation_negation_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write(!(true));
    }
    """, BufferInputOutputOperation())
    assert output.output == [False]


def test_operation_less_then_false():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 < 0));
    }
    """, BufferInputOutputOperation())
    assert output.output == [False]


def test_operation_less_then_false_equal():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 < 7));
    }
    """, BufferInputOutputOperation())
    assert output.output == [False]


def test_operation_less_then_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 < 10));
    }
    """, BufferInputOutputOperation())
    assert output.output == [True]


def test_operation_less_equal_then_false():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 <= 0));
    }
    """, BufferInputOutputOperation())
    assert output.output == [False]


def test_operation_less_equal_then_false_equal():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 <= 7));
    }
    """, BufferInputOutputOperation())
    assert output.output == [True]


def test_operation_less_equal_then_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 <= 10));
    }
    """, BufferInputOutputOperation())
    assert output.output == [True]


def test_operation_grater_then_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 > 0));
    }
    """, BufferInputOutputOperation())
    assert output.output == [True]


def test_operation_grater_then_false_equal():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 > 7));
    }
    """, BufferInputOutputOperation())
    assert output.output == [False]


def test_operation_grater_then_false():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 > 10));
    }
    """, BufferInputOutputOperation())
    assert output.output == [False]


def test_operation_grater_equal_then_true():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 >= 0));
    }
    """, BufferInputOutputOperation())
    assert output.output == [True]


def test_operation_grater_equal_then_false_equal():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 >= 7));
    }
    """, BufferInputOutputOperation())
    assert output.output == [True]


def test_operation_grater_equal_then_false():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        write((7 >= 10));
    }
    """, BufferInputOutputOperation())
    assert output.output == [False]


def test_operation_condition_variable():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        bool x = True;
        write((false && x));
    }
    """, BufferInputOutputOperation())
    assert output.output == [False]


def test_operation_condition_variable_wrong_type():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        int x = 7;
        write((false || x));
    }
    """, BufferInputOutputOperation())
    assert output.output == [True]


def test_assigment_unknown():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        x = (x + 1);
        write(x);
    }
    """, BufferInputOutputOperation([-2]))
    assert output.output == [-1]


def test_assigment_int_to_bool():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        int y = 10;
        y = (5 != 1);
        write(y);
    }
    """, BufferInputOutputOperation([-2]))
    assert output.output == [1]


def test_assigment_bool_to_int():
    output: BufferInputOutputOperation = Interpreter.interpret("""
    {
        bool x = false;
        x = (10 + 11);
        write(x);
    }
    """, BufferInputOutputOperation([-2]))
    assert output.output == [True]


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
        int i = 0;
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
