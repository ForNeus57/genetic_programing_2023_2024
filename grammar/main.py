from pathlib import Path
from random import seed

from src.genetic.evaluation.evaluation import FitnessFunction1_1_A, FitnessFunction1_1_B, FitnessFunction1_1_C, \
    FitnessFunction1_1_D, FitnessFunction1_1_E, FitnessFunction1_1_F, FitnessFunction1_2_A, FitnessFunction1_2_B, \
    FitnessFunction1_2_C, FitnessFunction1_2_D, FitnessFunction1_2_E, FitnessFunction1_3_A, FitnessFunction1_3_B, \
    FitnessFunction1_4_A, FitnessFunction1_4_B
from src.genetic.evolution.evolve import Evolution
from src.genetic.evaluation.generated.input_values_for_1_4_A import input_values
from src.genetic.individual.individual import Individual
from src.genetic.individual.structure.metadata import Metadata
from src.genetic.individual.structure.rules import Program, ExecutionBlock, LoopStatement, IfStatement, Condition, \
    Expression, Assigment, IOStatement, IOType
from src.genetic.individual.structure.tokens import BooleanToken, IntegerToken, VariableNameToken


def main() -> None:
    # evolution: Evolution = Evolution(
    #     FitnessFunction1_4_A(),
    #     input_values,
    # )
    # print(evolution.evolve())
    meta: Metadata = Metadata()
    meta.variables_scope.add('ADvd_')
    meta.variables_scope.add('gvr2')
    meta2: Metadata = Metadata(meta.variables_scope, meta.depth + 1)
    meta3: Metadata = Metadata(meta2.variables_scope, meta2.depth + 1)
    ind: Individual = Individual(
        Program(meta,
                ExecutionBlock(meta, [
                    LoopStatement(meta,
                                  Condition(meta,
                                            Condition(meta,
                                                      BooleanToken(False))),
                                  ExecutionBlock(meta2, [
                                      IfStatement(meta3,
                                                  Condition(meta2,
                                                            (
                                                                Condition(meta2,
                                                                          (
                                                                              Expression(meta2,
                                                                                         IntegerToken(1)),
                                                                              '==',
                                                                              Expression(meta2,
                                                                                         IntegerToken(12))
                                                                          )),
                                                                '&&',
                                                                Condition(meta2,
                                                                          (
                                                                              Condition(meta2,
                                                                                        BooleanToken(False)),
                                                                              '||',
                                                                              Condition(meta2,
                                                                                        BooleanToken(True))
                                                                          ))
                                                            )),
                                                  ExecutionBlock(meta3, [
                                                      IOStatement(meta2,
                                                                  IOType.WRITE,
                                                                  Expression(meta2,
                                                                             VariableNameToken('IGx_')),
                                                                  ),
                                                      IOStatement(meta2,
                                                                  IOType.READ,
                                                                  VariableNameToken('sZx')),
                                                  ]),
                                                  None),
                                      IfStatement(meta2,
                                                  Condition(meta,
                                                            (
                                                                Condition(meta,
                                                                          (
                                                                              Expression(meta,
                                                                                         IntegerToken(9)),
                                                                              '<',
                                                                              Expression(meta,
                                                                                         IntegerToken(24))
                                                                          )),
                                                                '||',
                                                                Condition(meta,
                                                                          (
                                                                              Condition(meta,
                                                                                        BooleanToken(False)),
                                                                              '&&',
                                                                              Condition(meta,
                                                                                        Condition(meta,
                                                                                        BooleanToken(True)))
                                                                          ))
                                                            )),
                                                  ExecutionBlock(meta3, [
                                                      Assigment(meta,
                                                                VariableNameToken('q_24'),
                                                                Expression(meta,
                                                                           (
                                                                               Expression(meta,
                                                                                          IntegerToken(9)),
                                                                               '+',
                                                                               Expression(meta,
                                                                                          (
                                                                                              Expression(meta,
                                                                                                         IntegerToken(
                                                                                                             2)),
                                                                                              '*',
                                                                                              Expression(meta,
                                                                                                         IntegerToken(
                                                                                                             4))
                                                                                          ))
                                                                           ))),
                                                  ]),
                                                  None),
                                      IOStatement(meta,
                                                  IOType.READ,
                                                  VariableNameToken('gvr2')),
                                      IOStatement(meta,
                                                  IOType.WRITE,
                                                  Expression(meta,
                                                             (
                                                                 Expression(meta,
                                                                            IntegerToken(61)),
                                                                 '*',
                                                                 Expression(meta,
                                                                            (
                                                                                Expression(meta,
                                                                                           IntegerToken(5)),
                                                                                '*',
                                                                                Expression(meta,
                                                                                           (
                                                                                               Expression(meta,
                                                                                                          IntegerToken(
                                                                                                              63)),
                                                                                               '+',
                                                                                               Expression(meta,
                                                                                                          IntegerToken(
                                                                                                              50))
                                                                                           ))
                                                                            ))
                                                             ))),
                                  ])
                                  ),
                    IfStatement(meta2,
                                Condition(meta,
                                          (
                                              Condition(meta,
                                                        BooleanToken(True)),
                                              '||',
                                              Condition(meta,
                                                        Condition(meta,
                                                                  (
                                                                      Expression(meta,
                                                                                 IntegerToken(-28)),
                                                                      '==',
                                                                      Expression(meta,
                                                                                 IntegerToken(-49))
                                                                  )))
                                          )),
                                ExecutionBlock(meta2, [
                                    Assigment(meta,
                                              VariableNameToken('ADvd_'),
                                              Expression(meta,
                                                         (
                                                             Expression(meta,
                                                                        IntegerToken(-12)),
                                                             '*',
                                                             Expression(meta,
                                                                        IntegerToken(28))
                                                         ))
                                              ),
                                    IOStatement(meta,
                                                IOType.WRITE,
                                                Expression(meta,
                                                           VariableNameToken('G'))),
                                    LoopStatement(meta3,
                                                  Condition(meta,
                                                            Condition(meta,
                                                                      BooleanToken(True))),
                                                  ExecutionBlock(meta3, [
                                                      IOStatement(meta,
                                                                  IOType.READ,
                                                                  VariableNameToken('C')),
                                                  ])),
                                ]),
                                ExecutionBlock(meta2, [
                                    IOStatement(meta3,
                                                IOType.READ,
                                                VariableNameToken('C')),

                                ]))
                ])
                ))
    print(ind)
    ind.save_to_file(Path('data/python/1_1_C/best_program38.pkl'))


if __name__ == '__main__':
    main()
