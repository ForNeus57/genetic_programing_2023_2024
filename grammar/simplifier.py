from sys import argv

from src.genetic.simplifier.simplifier import Simplifier


def cut_program_from_file(file_path: str) -> str:
    with open(file_path, 'r') as input_file:
        raw_input = input_file.readlines()

        return raw_input[-2].lstrip("Best Individual: ")


def main() -> None:
    # program: str = cut_program_from_file(argv[1])
    # simplifier: Simplifier = Simplifier(program)

    # simplifier: Simplifier = Simplifier("((1 * (3.2 + 3.4)) * 3)")
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier('(((cos((sin((0.15792111801538056 / ((sin((((cos(4.390922989460659)) - (cos((sin(((3.9378125013554417 - (4.567186184882816 + (4.9798113857157915 - (2.879804272999489 + 1.8159963035888813)))) * 1.636289987009465)))))) - 4.167758199134466))) - 2.0531718571910895)))))) / 2.637638162486309) + (1.6247319950636392 + (X1 * X1)))')
    # print(simplifier.simplify())

    simplifier: Simplifier = Simplifier('(0.3752679242505537 + (1.6247319950636392 + (X1 * X1)))')
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("(1 * ((( 3.2 + 3.4) / ( 3.3 + 3.3)) * 2))")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("(((sin(1)) + 1))")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("(((sin(1)) + X1))")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("((X1 * ( 3.2 + 3.4)) * 2)")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("((( 3.2 + 3.4) * X1) * 2)")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("((( 3.2 + 3.4) + X1) + 2)")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("(2 + (( 3.2 + 3.4) + X1))")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("(2 + (X1 + ( 3.2 + 3.4)))")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("((X1 * 5) * (sin((X1 + X1))))")
    print(simplifier.simplify())

    # with open(argv[2], 'w') as output_file:
    #     output_file.write(simplifier.simplify())


if __name__ == '__main__':
    main()
