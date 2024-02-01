from typing import Tuple, Union, Optional, Callable

from typing import Tuple, Union, Optional, Callable

def convert_output(gp_output: Union[Tuple[int, ...], Tuple[float, ...], Tuple[bool, ...]]) -> Tuple[int, ...]:
    return tuple([int(x) if not isinstance(x, bool) else int(x) for x in gp_output])

def create_fitness_function_for_1_1(target_value: int, check_first_only: bool, single_output_only: bool) -> Callable[[Tuple[int, ...]], int]:
    def fitness_function(gp_output: Tuple[int, ...]) -> int:
        if single_output_only and len(gp_output) != 1:
            return 9999999
        if check_first_only:
            return abs(gp_output[0] - target_value) if gp_output[0] != target_value else 0
        else:
            closest_value = min(gp_output, key=lambda x: abs(x - target_value))
            return abs(closest_value - target_value) if target_value not in gp_output else 0
    return fitness_function

def create_fitness_function_for_numerical_operations(operation: Callable[[Tuple[int, ...]], int]) -> Callable[[Tuple[int, ...], Tuple[int, ...]], int]:
    def fitness_function(gp_output: Tuple[int, ...], gp_input: Tuple[int, ...]) -> int:
        if len(gp_output) != 1:
            return 9999999
        expected_result = operation(gp_input)
        return abs(gp_output[0] - expected_result)
    return fitness_function

def create_fitness_function_for_vector_operations(operation: Callable[[Tuple[int, ...]], Tuple[int, ...]]) -> Callable[[Tuple[int, ...], Tuple[int, ...]], int]:
    def fitness_function(gp_output: Tuple[int, ...], gp_input: Tuple[int, ...]) -> int:
        expected_result = operation(gp_input)
        if len(gp_output) != len(expected_result):
            return 9999999
        return sum(abs(o - e) for o, e in zip(gp_output, expected_result))
    return fitness_function

def sum_operation(gp_input: Tuple[int, ...]) -> int:
    return sum(gp_input[:2])

def diff_operation(gp_input: Tuple[int, ...]) -> int:
    return gp_input[0] - gp_input[1]

def mul_operation(gp_input: Tuple[int, ...]) -> int:
    return gp_input[0] * gp_input[1]

def max_operation(gp_input: Tuple[int, ...]) -> int:
    return max(gp_input[:2])

def average_operation(include_first: bool, gp_input: Tuple[int, ...]) -> int:
    inputs = gp_input[:10] if include_first else gp_input[1:gp_input[0] + 1]
    return int(sum(inputs) / len(inputs))

def sum_int_and_simulated_float(gp_input: Tuple[int, ...]) -> float:
    float_to_add = gp_input[1] + (gp_input[2] / 10 ** len(str(gp_input[2])))
    return gp_input[0] + float_to_add

def negative_to_zero_operation(gp_input: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(x if x >= 0 else 0 for x in gp_input)

def smallest_operation(gp_input: Tuple[int, ...]) -> int:
    if len(gp_input) != 4:
        return 9999999
    return min(gp_input)


fitness_functions = {
    "1.1.A": create_fitness_function_for_1_1(1, False, False),
    "1.1.B": create_fitness_function_for_1_1(789, False, False),
    "1.1.C": create_fitness_function_for_1_1(31415, False, False),
    "1.1.D": create_fitness_function_for_1_1(1, True, False),
    "1.1.E": create_fitness_function_for_1_1(789, True, False),
    "1.1.F": create_fitness_function_for_1_1(1, False, True),
    "1.2.A": create_fitness_function_for_numerical_operations(sum_operation),
    "1.2.B": create_fitness_function_for_numerical_operations(sum_operation),
    "1.2.C": create_fitness_function_for_numerical_operations(sum_operation),
    "1.2.D": create_fitness_function_for_numerical_operations(diff_operation),
    "1.2.E": create_fitness_function_for_numerical_operations(mul_operation),
    "1.3.A": create_fitness_function_for_numerical_operations(max_operation),
    "1.3.B": create_fitness_function_for_numerical_operations(max_operation),
    "1.4.A": create_fitness_function_for_numerical_operations(lambda x: average_operation(False, x)),
    "1.4.B": create_fitness_function_for_numerical_operations(lambda x: average_operation(True, x)),
    "B.1": create_fitness_function_for_numerical_operations(sum_int_and_simulated_float),
    "B.15": create_fitness_function_for_vector_operations(negative_to_zero_operation),
    "B.28": create_fitness_function_for_numerical_operations(smallest_operation)
}
