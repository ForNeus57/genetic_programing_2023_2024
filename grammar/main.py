from src.utils import read_input_params, read_config, read_input_data
from src.genetic.individual.individual import Individual


def main():
    # params = read_input_params("data/xmxp2.dat")
    # config = read_config("data/config.json")
    # data = read_input_data("data/xmxp2.dat", params["nvar"])
    #
    # random_tree = generate_random_tree(config["DEPTH"], params["minrand"], params["maxrand"])
    # print("Wygenerowane losowe drzewo:")
    # print(random_tree)

    ind = Individual.from_random()
    print(ind)


if __name__ == "__main__":
    main()
