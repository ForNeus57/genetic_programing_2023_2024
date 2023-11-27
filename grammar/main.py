from src.utils import read_input_params, read_config, read_input_data
from src.genetic_programming.generator import generate_random_tree

def main():
    params = read_input_params("data/xmxp2.dat")
    config = read_config("data/config.json")
    data = read_input_data("data/xmxp2.dat", params["nvar"])

    random_tree = generate_random_tree(config["DEPTH"], params["minrand"], params["maxrand"])
    print("Wygenerowane losowe drzewo:")
    print(random_tree)
    print("Data:")
    print(data)

if __name__ == "__main__":
    main()