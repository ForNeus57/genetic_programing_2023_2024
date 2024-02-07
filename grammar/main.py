from random import seed
from time import perf_counter

from src.genetic.evaluation.evaluation import FitnessFunction1_1_C, FitnessFunction1_1_D, FitnessFunction1_1_E, \
    FitnessFunction1_1_F, FitnessFunction1_1_A, FitnessFunction1_1_B, FitnessFunction1_2_A, FitnessFunction1_2_B, \
    FitnessFunction1_2_C, FitnessFunction1_2_D, FitnessFunction1_2_E, FitnessFunction1_3_A, FitnessFunction1_3_B, \
    FitnessFunction1_4_A, FitnessFunction1_4_B
from src.genetic.evaluation.generated.input_values_for_1_4_B import input_values
from src.genetic.evolution.evolve import Evolution
from src.genetic.evolution.population import Population
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
    # seed(100)
    # import sys
    # ind = Individual.from_random()
    # print(sys.getsizeof(ind))
    # print(sys.getsizeof(str(ind)))
    # evolution: Evolution = Evolution(
    #     FitnessFunction1_4_B(),
    #     input_values,
    # )
    # print(evolution.evolve())
    # ind = Individual.from_random()
    # print(ind)
    # print(Population.from_ramped_half_and_half(50).individuals)
    # ind = Individual.from_random()
    # print(ind)
    # ind.mutate()
    # print(ind)
    print(
        Interpreter.interpret(
            """
              {
	bttfz = ((39 * 20) - -8);
	write(bttfz);
	while ((10 > bttfz)) {
		while (true) {
			read(LpF);
			read(bttfz);
			read(o);
			bH = 23;
		}
		while ((-1 <= -46)) {
			write(56);
			bttfz = bttfz;
			T = -10;
			write(-5);
		}
		while (((bttfz >= bttfz) || !(true))) {
			read(bttfz);
			bttfz = bttfz;
		}
		cB = bttfz;
	}
	if (true) {
		while (!(!(true))) {
			write((bttfz - -1));
			read(D5jZ8);
			write(-35);
		}
		read(OfE);
		while (!(!(true))) {
			read(Fy);
			bttfz = -51;
			bttfz = ((Fy / Fy) - (bttfz * -47));
			write(Fy);
		}
	}
}


            """,
            BufferInputOutputOperation()
        ).output
    )
    
#     print(
#         Interpreter.interpret(
#             """
#             {
# 		while (((false || true) || true)) {
# 			rl = ((30 * rl) * (rl - 46));
# 			zK = rl;
# 		}
# }
# """,
#             BufferInputOutputOperation()
#         )
#     )
    # print(Individual.from_random())
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
