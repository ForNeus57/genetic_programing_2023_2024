from typing import List, Union, Optional

def convert_output(gp_output: List[Union[int, float, bool]]) -> List[float]:
    """
    Function converts output of genetic program to list of floats.
    Boolean values are converted to 0.0 and 1.0.
    """
    return [float(x) if not isinstance(x, bool) else float(int(x)) for x in gp_output]

def evaluate_gp_performance(gp_output: Union[List[int], List[float], List[bool]], test_case: str, gp_input: Optional[List[int]] = None) -> float:
    """
    Function evaluates performance of genetic program.

    Args:
        gp_output: Output of genetic program.
        test_case: Test case to evaluate.
        gp_input: Input of genetic program.

    Returns:
        The evaluation result as a non-negative integer or float.
    """
    gp_output = convert_output(gp_output)
    fitness = 0

    if test_case.startswith("1.1"):
        fitness = evaluate_scenario_1_1(gp_output, test_case)
    elif test_case.startswith("1.2"):
        fitness = evaluate_scenario_1_2(gp_output, test_case, gp_input)
    elif test_case.startswith("1.3"):
        fitness = evaluate_scenario_1_3(gp_output, test_case, gp_input)
    elif test_case.startswith("1.4"):
        fitness = evaluate_scenario_1_4(gp_output, test_case, gp_input)
    return fitness

def evaluate_scenario_1_1(gp_output: List[float], test_case: str) -> float:
    fitness = 0

    if test_case in ["1.1.A", "1.1.B", "1.1.C"]:
        target_value = {
            "1.1.A": 1,
            "1.1.B": 789,
            "1.1.C": 31415
        }[test_case]
        closest_value = min(gp_output, key=lambda x: abs(x - target_value))
        fitness += abs(closest_value - target_value) if target_value not in gp_output else 0
    elif test_case in ["1.1.D", "1.1.E"]:
        first_position_value = {
            "1.1.D": 1,
            "1.1.E": 789
        }[test_case]
        fitness += abs(gp_output[0] - first_position_value) if gp_output[0] != first_position_value else 0
    elif test_case == "1.1.F":
        if len(gp_output) == 1:
            fitness += abs(gp_output[0] - 1) if gp_output[0] != 1 else 0
        else:
            fitness += 9999999

    return fitness

def evaluate_scenario_1_2(gp_output: List[float], test_case: str, gp_input: List[int]) -> float:
    fitness = 0

    expected_result = None
    if test_case in ["1.2.A", "1.2.B", "1.2.C"]:
        expected_result = sum(gp_input[:2])
    elif test_case == "1.2.D":
        expected_result = gp_input[0] - gp_input[1]
    elif test_case == "1.2.E":
        expected_result = gp_input[0] * gp_input[1]

    actual_result = gp_output[0]
    if len(gp_output) != 1:
        fitness += 9999999
    else:
        fitness += abs(actual_result - expected_result) if actual_result != expected_result else 0

    return fitness

def evaluate_scenario_1_3(gp_output: List[float], test_case: str, gp_input: List[int]) -> float:
    fitness = 0

    expected_result = None
    if test_case in ["1.3.A", "1.3.B"]:
        expected_result = max(gp_input[:2])

    actual_result = gp_output[0]
    if len(gp_output) != 1:
        fitness += 9999999
    else:
        fitness += abs(actual_result - expected_result) if actual_result != expected_result else 0

    return fitness

def evaluate_scenario_1_4(gp_output: List[float], test_case: str, gp_input: List[int]) -> float:
    fitness = 0

    expected_result = None
    if test_case == "1.4.A":
        expected_result = sum(gp_input[:10]) / 10
    elif test_case == "1.4.B":
        expected_result = sum(gp_input[1:gp_input[0] + 1]) / gp_input[0]

    actual_result = gp_output[0]
    if len(gp_output) != 1:
        fitness += 9999999
    else:
        fitness += abs(actual_result - expected_result) if actual_result != expected_result else 0

    return fitness
