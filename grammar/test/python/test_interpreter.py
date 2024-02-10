from src.genetic.individual.individual import Individual
from src.genetic.individual.structure.metadata import Metadata
from src.genetic.individual.structure.rules import Program, ExecutionBlock, IOStatement, IOType, Expression, Assigment, \
    IfStatement, Condition, LoopStatement
from src.genetic.individual.structure.tokens import VariableNameToken, IntegerToken, BooleanToken
from src.genetic.interpreter.input_output import BufferInputOutputOperation
from src.genetic.interpreter.interpreter import Interpreter


def test_write_unknown():
    """
    {
        write(x);
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IOStatement(meta,
                                IOType.WRITE,
                                Expression(meta,
                                           VariableNameToken('x')
                                           )
                                )
                ])
                )
    )
    assert ind.execute((-37,)) == [-37]


def test_write_int():
    """
    {
        write(-555);
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IOStatement(meta,
                                IOType.WRITE,
                                Expression(meta,
                                           IntegerToken(
                                               -555
                                           )
                                           )
                                )
                ])
                )
    )
    assert ind.execute() == [-555]


def test_write_expression():
    """
    {
        write(((7 + 4) / 3));
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IOStatement(meta,
                                IOType.WRITE,
                                Expression(meta,
                                           (
                                               Expression(meta,
                                                          (
                                                              Expression(meta,
                                                                         IntegerToken(
                                                                             7
                                                                         )
                                                                         ),
                                                              '+',
                                                              Expression(meta,
                                                                         IntegerToken(
                                                                             4
                                                                         )
                                                                         )
                                                          )
                                                          ),
                                               '/',
                                               Expression(meta,
                                                          IntegerToken(
                                                              3
                                                          )
                                                          )
                                           )
                                           )
                                )
                ])
                )
    )
    assert ind.execute() == [3]


def test_read_unknown():
    """
    {
        read(x);
        x = (x + 1);
        write(x);
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IOStatement(meta,
                                IOType.READ,
                                VariableNameToken(
                                    'x'
                                )
                                ),
                    Assigment(meta,
                              VariableNameToken(
                                  'x'
                              ),
                              Expression(meta,
                                         (
                                             Expression(meta,
                                                        VariableNameToken(
                                                            'x'
                                                        )
                                                        ),
                                             '+',
                                             Expression(meta,
                                                        IntegerToken(
                                                            22
                                                        )
                                                        )
                                         )
                                         )
                              ),
                    IOStatement(meta,
                                IOType.WRITE,
                                Expression(meta,
                                           VariableNameToken(
                                               'x'
                                           )
                                           )
                                )
                ])
                )
    )
    assert ind.execute((-444,)) == [-422]


def test_read_int():
    """
    {
        x = -3;
        read(x);
        write(x);
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    Assigment(meta,
                              VariableNameToken(
                                  'x'
                              ),
                              Expression(meta,
                                         IntegerToken(
                                             -3
                                         )
                                         )
                              ),
                    IOStatement(meta,
                                IOType.READ,
                                VariableNameToken(
                                    'x'
                                )
                                ),
                    IOStatement(meta,
                                IOType.WRITE,
                                Expression(meta,
                                           VariableNameToken(
                                               'x'
                                           )
                                           )
                                )
                ])
                )
    )
    assert ind.execute((17,)) == [17]


def test_operation_add():
    """
    {
        write((7 + 11));
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IOStatement(meta,
                                IOType.WRITE,
                                Expression(meta,
                                           (
                                               Expression(meta,
                                                          IntegerToken(
                                                              7
                                                          )
                                                          ),
                                               '+',
                                               Expression(meta,
                                                          IntegerToken(
                                                              11
                                                          )
                                                          )
                                           )
                                           ),
                                )
                ])
                )
    )
    assert ind.execute() == [18]


def test_operation_subtract():
    """
    {
        write((7 - 11));
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IOStatement(meta,
                                IOType.WRITE,
                                Expression(meta,
                                           (
                                               Expression(meta,
                                                          IntegerToken(
                                                              7
                                                          )
                                                          ),
                                               '-',
                                               Expression(meta,
                                                          IntegerToken(
                                                              11
                                                          )
                                                          )
                                           )
                                           ),
                                )
                ])
                )
    )
    assert ind.execute() == [-4]


def test_operation_multiply():
    """
    {
        write((7 * -11));
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IOStatement(meta,
                                IOType.WRITE,
                                Expression(meta,
                                           (
                                               Expression(meta,
                                                          IntegerToken(
                                                              7
                                                          )
                                                          ),
                                               '*',
                                               Expression(meta,
                                                          IntegerToken(
                                                              -11
                                                          )
                                                          )
                                           )
                                           ),
                                )
                ])
                )
    )
    assert ind.execute() == [-77]


def test_operation_divide():
    """
    {
        write((7 / -11));
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IOStatement(meta,
                                IOType.WRITE,
                                Expression(meta,
                                           (
                                               Expression(meta,
                                                          IntegerToken(
                                                              7
                                                          )
                                                          ),
                                               '/',
                                               Expression(meta,
                                                          IntegerToken(
                                                              -11
                                                          )
                                                          )
                                           )
                                           ),
                                )
                ])
                )
    )
    assert ind.execute() == [-1]


def test_operation_divide_by_zero():
    """
    {
        write((7 / 0));
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IOStatement(meta,
                                IOType.WRITE,
                                Expression(meta,
                                           (
                                               Expression(meta,
                                                          IntegerToken(
                                                              7
                                                          )
                                                          ),
                                               '/',
                                               Expression(meta,
                                                          IntegerToken(
                                                              0
                                                          )
                                                          )
                                           )
                                           ),
                                )
                ])
                )
    )
    assert ind.execute() == [7]


def test_operation_negation_false():
    """
    {
        if (!(false)) {
            write(1);
        } else {
            write(0);
        }
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          Condition(meta, BooleanToken(
                                              False
                                          ))
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [1]


def test_operation_negation_true():
    """
    {
        if (!(true)) {
            write(1);
        } else {
            write(0);
        }
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          Condition(meta, BooleanToken(
                                              True
                                          ))
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [0]


def test_operation_less_then_false():
    """
    {
        if ((7 < 0)) {
            write(1);
        } else {
            write(0);
        }
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '<',
                                              Expression(meta,
                                                         IntegerToken(
                                                             0
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [0]


def test_operation_less_then_false_equal():
    """
    {
        if ((7 < 7)) {
            write(1);
        } else {
            write(0);
        }
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '<',
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [0]


def test_operation_less_then_true():
    """
    {
        if ((7 < 10)) {
            write(1);
        } else {
            write(0);
        }
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '<',
                                              Expression(meta,
                                                         IntegerToken(
                                                             10
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [1]


def test_operation_less_equal_then_false():
    """
        {
            if ((7 <= 0)) {
                write(1);
            } else {
                write(0);
            }
        }
        """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '<=',
                                              Expression(meta,
                                                         IntegerToken(
                                                             0
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [0]


def test_operation_less_equal_then_false_equal():
    """
        {
            if ((7 <= 7)) {
                write(1);
            } else {
                write(0);
            }
        }
        """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '<=',
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [1]


def test_operation_less_equal_then_true():
    """
        {
            if ((7 <= 10)) {
                write(1);
            } else {
                write(0);
            }
        }
        """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '<=',
                                              Expression(meta,
                                                         IntegerToken(
                                                             10
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [1]


def test_operation_grater_then_true():
    """
    {
        if ((7 > 0)) {
            write(1);
        } else {
            write(0);
        }
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '>',
                                              Expression(meta,
                                                         IntegerToken(
                                                             0
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [1]


def test_operation_grater_then_false_equal():
    """
        {
            if ((7 > 7)) {
                write(1);
            } else {
                write(0);
            }
        }
        """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '>',
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [0]


def test_operation_grater_then_false():
    """
    {
        if ((7 > 10)) {
            write(1);
        } else {
            write(0);
        }
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '>',
                                              Expression(meta,
                                                         IntegerToken(
                                                             10
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [0]


def test_operation_grater_equal_then_true():
    """
            {
                if ((7 >= 0)) {
                    write(1);
                } else {
                    write(0);
                }
            }
            """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '>=',
                                              Expression(meta,
                                                         IntegerToken(
                                                             0
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [1]


def test_operation_grater_equal_then_false_equal():
    """
    {
        if ((7 >= 7)) {
            write(1);
        } else {
            write(0);
        }
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '>=',
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [1]


def test_operation_grater_equal_then_false():
    """
            {
                if ((7 >= 10)) {
                    write(1);
                } else {
                    write(0);
                }
            }
            """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    IfStatement(meta,
                                Condition(meta,
                                          (
                                              Expression(meta,
                                                         IntegerToken(
                                                             7
                                                         )
                                                         ),
                                              '>=',
                                              Expression(meta,
                                                         IntegerToken(
                                                             10
                                                         )
                                                         )
                                          )
                                          ),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               1
                                                           )
                                                           )
                                                )
                                ]),
                                ExecutionBlock(meta, [
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           IntegerToken(
                                                               0
                                                           )
                                                           )
                                                )
                                ])
                                )
                ])
                )
    )
    assert ind.execute() == [0]


def test_assigment_unknown():
    """
    {
        x = (x + 1);
        write(x);
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    Assigment(meta,
                              VariableNameToken(
                                  'x'
                              ),
                              Expression(meta,
                                         (
                                             Expression(meta,
                                                        VariableNameToken(
                                                            'x'
                                                        )),
                                             '+',
                                             Expression(meta,
                                                        IntegerToken(
                                                            1
                                                        ))
                                         )
                                         )),
                    IOStatement(meta,
                                IOType.WRITE,
                                Expression(meta,
                                           VariableNameToken(
                                               'x'
                                           )
                                           ))
                ])
                )
    )
    assert ind.execute((-2,)) == [-1]


def test_loop_infinite():
    """
    {
        while (true) {
            write(15);
        }
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    LoopStatement(meta,
                                  Condition(meta,
                                            BooleanToken(
                                                True
                                            )
                                            ),
                                  ExecutionBlock(meta, [
                                      IOStatement(meta,
                                                  IOType.WRITE,
                                                  Expression(meta,
                                                             IntegerToken(
                                                                 15
                                                             )
                                                             ))
                                  ])
                                  )

                ]))
    )
    output: list = ind.execute((-2,))
    assert len(output) > 1
    assert 15 in output


def test_loop_true():
    """
    {
        i = 0;
        while ((i < 5)) {
            write(i);
            i = (i + 1);
        }
    }
    """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    Assigment(meta,
                              VariableNameToken(
                                  'i'
                              ),
                              Expression(meta,
                                         IntegerToken(
                                             0
                                         )
                                         )
                              ),
                    LoopStatement(meta,
                                  Condition(meta,
                                            (
                                                Expression(meta,
                                                           VariableNameToken(
                                                               'i'
                                                           )
                                                           ),
                                                '<',
                                                Expression(meta,
                                                           IntegerToken(
                                                               5
                                                           )
                                                           )
                                            )
                                            ),
                                  ExecutionBlock(meta, [
                                      IOStatement(meta,
                                                  IOType.WRITE,
                                                  Expression(meta,
                                                             VariableNameToken(
                                                                 'i'
                                                             )
                                                             )),
                                      Assigment(meta,
                                                VariableNameToken(
                                                    'i'
                                                ),
                                                Expression(meta,
                                                           (
                                                               Expression(meta,
                                                                          VariableNameToken(
                                                                              'i'
                                                                          )
                                                                          ),
                                                               '+',
                                                               Expression(meta,
                                                                          IntegerToken(
                                                                              1
                                                                          ))
                                                           )
                                                           )

                                                )
                                  ])
                                  )

                ]))
    )
    assert ind.execute() == [0, 1, 2, 3, 4]


def test_loop_false():
    """
        {
            while (false) {
                write(15);
            }
        }
        """
    meta: Metadata = Metadata.from_dummy()
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    LoopStatement(meta,
                                  Condition(meta,
                                            BooleanToken(
                                                False
                                            )
                                            ),
                                  ExecutionBlock(meta, [
                                      IOStatement(meta,
                                                  IOType.WRITE,
                                                  Expression(meta,
                                                             IntegerToken(
                                                                 15
                                                             )
                                                             ))
                                  ])
                                  )

                ]))
    )
    output: list = ind.execute((-2,))
    assert output == []
