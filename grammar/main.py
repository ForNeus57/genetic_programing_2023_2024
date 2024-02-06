from time import perf_counter

from src.genetic.evaluation.evaluation import FitnessFunction1_1_A, FitnessFunction1_1_B
from src.genetic.evolution.evolve import Evolution
from src.genetic.individual.individual import Individual


def execute(inds: tuple[Individual]):
    for ind in inds:
        try:
            start = perf_counter()
            output = ind.execute((1, False))
            total = perf_counter() - start
            print(total, output)
        except Exception as error:
            print("Error!", error, str(ind))


def main():
    # seed(8)
    # import sys
    # ind = Individual.from_random()
    # print(sys.getsizeof(ind))
    # print(sys.getsizeof(str(ind)))
    evolution: Evolution = Evolution(
        FitnessFunction1_1_B(),
        [tuple()],
    )
    print(evolution.evolve())
    # params = read_input_params("data/xmxp2.dat")
    # config = read_config("data/config.json")
    # data = read_input_data("data/xmxp2.dat", params["nvar"])

    # random_tree = generate_random_tree(config["DEPTH"], params["minrand"], params["maxrand"])
    # print("Wygenerowane losowe drzewo:")
    # print(random_tree)
    # seed(8)

    # print("ind1")
    # ind = Individual.from_random()
    # print(ind)
    # # print(ind, len(ind))
    #
    # print("mutation")
    # ind.mutate()
    # print(ind)
    # size: int = 25_000
    # processes: int = 10
    #
    # start = perf_counter()
    # pop = Population.from_ramped_half_and_half(size)
    # # print(pop.individuals)
    # print(len(pop.individuals), perf_counter() - start)
    # # avg = 0.
    # computation_start = perf_counter()
    #
    # with Pool(processes) as pool:
    #     pool.imap(execute, pop.individuals, 40)
    #
    # print(perf_counter() - computation_start)
    # print(IOStatement.from_random(Metadata()))

    # ind.mutate()
    # print(ind)
    # print("ind2")
    # ind2 = Individual.from_random()
    # print(ind2, len(ind2))
    #
    # print("croos ind 1")
    # ind.crossover(ind2)
    # print(ind, len(ind))
    #
    # print("cross ind 2")
    # print(ind2, len(ind2))

    # out = Interpreter.interpret(str(ind), BufferInputOutputOperation([1, False]), False)
    # out = out[0]
    # if out is not None:
    #     print(out.output)
    # else:
    #     print("None")

    # print(Interpreter.interpret("./test/resources/test4.mgp", BufferInputOutputOperation([False, 1, 5, True]), True))


if __name__ == "__main__":
    main()
