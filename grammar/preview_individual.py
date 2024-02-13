from pathlib import Path
from sys import argv

from src.genetic.evaluation.evaluation import FitnessFunction1_1_A, FitnessFunction1_1_B
from src.genetic.individual.individual import Individual
from src.genetic.interpreter.context import InterpreterContext
from src.genetic.interpreter.input_output import ConsoleInputOutputOperation, BufferInputOutputOperation


def main() -> None:
    if len(argv) != 2:
        print(f'Usage: {argv[0]} <filename>.pkl')
        exit(1)

    filename: Path = Path(argv[1])
    if not filename.exists():
        print(f'File does not exist: {filename}')
        exit(2)

    individual: Individual = Individual.from_file(filename)
    print(individual)
    output: BufferInputOutputOperation = BufferInputOutputOperation((0,))
    try:
        individual.program.visit(InterpreterContext(output))
    except StopIteration:
        pass
    print(output.output)
    print(FitnessFunction1_1_B().calculate_fitness(
        tuple(output.output),
    ))


if __name__ == '__main__':
    main()
