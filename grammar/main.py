from src.genetic.individual.individual import Individual
from random import seed

from src.genetic.interpreter.input_output import BufferInputOutputOperation
from src.genetic.interpreter.interpreter import Interpreter


def main():
    # params = read_input_params("data/xmxp2.dat")
    # config = read_config("data/config.json")
    # data = read_input_data("data/xmxp2.dat", params["nvar"])
    #
    # random_tree = generate_random_tree(config["DEPTH"], params["minrand"], params["maxrand"])
    # print("Wygenerowane losowe drzewo:")
    # print(random_tree)

    # Interpreter.interpret("./test/resources/test1.mgp", BufferInputOutputOperation([1, False]))
    # seed(6)

    ind = Individual.from_random()
    print(ind)


if __name__ == "__main__":
    main()
