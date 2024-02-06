from random import seed
from time import perf_counter

from src.genetic.evaluation.evaluation import FitnessFunction1_1_A, FitnessFunction1_1_B
from src.genetic.evolution.evolve import Evolution
from src.genetic.individual.individual import Individual
from src.genetic.interpreter.input_output import BufferInputOutputOperation
from src.genetic.interpreter.interpreter import Interpreter


def execute(inds: tuple[Individual]):
    for ind in inds:
        try:
            start = perf_counter()
            output = ind.execute((1, False))
            total = perf_counter() - start
            print(total, output)
        except Exception as error:
            print("Error!", error, str(ind))


def main() -> None:
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
#     grade = FitnessFunction1_1_B()
#     print(grade.calculate_fitness(Interpreter.interpret(
#         """
#          {
# 	while ((-28 != 50)) {
# 		bool YXZb = (true || false);
# 		YXZb = (YXZb && true);
# 		read(YXZb);
# 		write((41 == 54));
# 	}
# 	if (!(true)) {
# 		int FM = (3 + 39);
# 		int dr = (FM - -7);
# 		read(FM);
# 	} else {
# 		write((44 + -53));
# 		write((-15 <= -15));
# 		write((-21 + 52));
# 		bool z = (false && true);
# 		bool Vd2 = !(z);
# 	}
# 	if ((-57 != -33)) {
# 		int jZ2 = (2 + 60);
# 		bool Cx_s = (false || false);
# 		int refd = (47 * 44);
# 		read(Cx_s);
# 		Cx_s = !(Cx_s);
# 	} else {
# 		int O = (-13 / -48);
# 		int QRLP = (O + -9);
# 	}
# 	if (!(false)) {
# 		bool sdDx7 = (false || true);
# 		sdDx7 = (-63 >= -41);
# 		sdDx7 = !(sdDx7);
# 		int NB = (22 / 5);
# 		write((sdDx7 || true));
# 	} else {
# 		bool zDC = !(true);
# 		zDC = (27 >= 46);
# 		zDC = (17 == -5);
# 		int lTG = (-53 + -45);
# 		int qHs8 = (14 - -11);
# 	}
# }
#         """,
#         BufferInputOutputOperation(),
#     ).output, tuple()))

    # ind = Individual.from_random()
    # print(ind)
    # ind.mutate()
    # print(ind)

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
