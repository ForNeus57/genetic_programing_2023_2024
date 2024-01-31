from src.genetic.individual.individual import Individual
from random import seed

from src.genetic.interpreter.input_output import BufferInputOutputOperation, ConsoleInputOutputOperation
from src.genetic.interpreter.interpreter import Interpreter


def main():
    # params = read_input_params("data/xmxp2.dat")
    # config = read_config("data/config.json")
    # data = read_input_data("data/xmxp2.dat", params["nvar"])
    #
    # random_tree = generate_random_tree(config["DEPTH"], params["minrand"], params["maxrand"])
    # print("Wygenerowane losowe drzewo:")
    # print(random_tree)
    # seed(8)
    #
    # ind = Individual.from_random()
    # print(ind)
    #
    # ind.mutate()
    # print(ind)
    # ind2 = Individual.from_random()
    # print(ind2)
    # ind.crossover(ind2)
    # print(ind)

    # out = Interpreter.interpret(str(ind), BufferInputOutputOperation([1, False]), False)
    # out = out[0]
    # if out is not None:
    #     print(out.output)
    # else:
    #     print("None")

    print(Interpreter.interpret("./test/resources/test4.mgp", BufferInputOutputOperation([False, 1, 5, True]), True))


if __name__ == "__main__":
    main()
