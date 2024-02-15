from pathlib import Path
from random import seed

from src.genetic.evaluation.evaluation import FitnessFunction1_1_A, FitnessFunction1_1_B, FitnessFunction1_1_C, \
    FitnessFunction1_1_D, FitnessFunction1_1_E, FitnessFunction1_1_F, FitnessFunction1_2_A, FitnessFunction1_2_B, \
    FitnessFunction1_2_C, FitnessFunction1_2_D, FitnessFunction1_2_E, FitnessFunction1_3_A, FitnessFunction1_3_B, \
    FitnessFunction1_4_A, FitnessFunction1_4_B, FitnessFunction1_4_A_1, FitnessFunction1_4_B_1, FitnessFunctionB_1, \
    FitnessFunctionB_21, FitnessFunctionB_28, FitnessFunctionBool, FitnessFunction1_4_A_2, FitnessFunctionB_21_1, \
    FitnessFunction1_4_B_2, generate_truth_tables, FitnessFunctionBool1, FitnessFunctionBool2, FitnessFunctionB_1_1, \
    FitnessFunctionB_28_1, FitnessFunctionB_21_2, FitnessFunctionB_1_2
from src.genetic.evolution.evolve import Evolution
from src.genetic.evaluation.generated.input_values_for_B_1 import input_values


def main() -> None:
    # seed(0)
    # grader: FitnessFunctionBool = FitnessFunctionBool(10)
    evolution: Evolution = Evolution(
        # FitnessFunctionBool2(),
        # generate_truth_tables(2),
        FitnessFunctionB_1_2(),
        input_values,
    )
    print(evolution.evolve())


if __name__ == '__main__':
    main()
