"""
1.1.A Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 1. Poza liczbą 1 może też zwrócić inne liczby.

1.1.B Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 789. Poza liczbą 789 może też zwrócić inne liczby.

1.1.C Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 31415. Poza liczbą 31415 może też zwrócić inne liczby.

1.1.D Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1. Poza liczbą 1 może też zwrócić inne liczby.

1.1.E Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 789. Poza liczbą 789 może też zwrócić inne liczby.

1.1.F Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę 1. Poza liczbą 1 NIE powinien nic więcej wygenerować.

1.2.A Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]

1.2.B Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9]

1.2.C Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]

1.2.D Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich różnicę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]

1.2.E Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich iloczyn. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]

1.3.A Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) większą z nich. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]

1.3.B Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) większą z nich. Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999]

1.4.A Program powinien odczytać dziesięć pierwszych liczy z wejścia i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną (zaokrągloną do pełnej liczby całkowitej). Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99]

1.4.B Program powinien odczytać na początek z wejścia pierwszą liczbę (ma być to wartość nieujemna) a następnie tyle liczb (całkowitych) jaka jest wartość pierwszej odczytanej liczby i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną zaokrągloną do pełnej liczby całkowitej (do średniej nie jest wliczana pierwsza odczytana liczba, która mówi z ilu liczb chcemy obliczyć średnią). Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99], pierwsza liczba może być tylko w zakresie [0,99].

B.1 Given an integer and a float, print their sum.

B.21 Given a vector of integers, return the vector where all negative integers have been replaced by 0.

B.28 Given four integers, print the smallest of them.
"""

from typing import Tuple, Union, Optional, Callable
from abc import ABC, abstractmethod
from itertools import product

class FitnessFunctionBase(ABC):
    def convert_output(self, gp_output: Union[Tuple[int, ...], Tuple[float, ...], Tuple[bool, ...], None]) -> Tuple[int, ...]:
        if gp_output is None:
            return tuple()
        return tuple(int(x) if not isinstance(x, bool) else int(x) for x in gp_output)
    
    def calculate_fitness(self, gp_output: Union[Tuple[int, ...], Tuple[float, ...], Tuple[bool, ...], None], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        if gp_output is None or len(gp_output) == 0:  # Sprawdza, czy wyjście jest puste lub None tylko raz
            return 9999999  # Zwraca dużą wartość kary dla pustego wyjścia
        converted_output = self.convert_output(gp_output)
        return self._calculate_fitness_impl(converted_output, gp_input)
    
    @abstractmethod
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        pass

class FitnessFunction1_1_A(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        closest_value = min(gp_output, key=lambda x: abs(x - 1))
        return abs(closest_value - 1) if 1 not in gp_output else 0
    
class FitnessFunction1_1_B(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        closest_value = min(gp_output, key=lambda x: abs(x - 789))
        return abs(closest_value - 789) if 789 not in gp_output else 0
    
class FitnessFunction1_1_C(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        closest_value = min(gp_output, key=lambda x: abs(x - 31415))
        return abs(closest_value - 31415) if 31415 not in gp_output else 0
    
class FitnessFunction1_1_D(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        return abs(gp_output[0] - 1) if gp_output[0] != 1 else 0
    
class FitnessFunction1_1_E(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        return abs(gp_output[0] - 789) if gp_output[0] != 789 else 0
    
class FitnessFunction1_1_F(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        return 0 if len(gp_output) == 1 and gp_output[0] == 1 else 9999999
    
class FitnessFunction1_2_A(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        expected_result = sum(gp_input[:2])
        return abs(gp_output[0] - expected_result) if len(gp_output) == 1 else 9999999
    
class FitnessFunction1_2_B(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        expected_result = sum(gp_input[:2])
        return abs(gp_output[0] - expected_result) if len(gp_output) == 1 else 9999999
    
class FitnessFunction1_2_C(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        expected_result = sum(gp_input[:2])
        return abs(gp_output[0] - expected_result) if len(gp_output) == 1 else 9999999
    
class FitnessFunction1_2_D(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        expected_result = gp_input[0] - gp_input[1]
        return abs(gp_output[0] - expected_result) if len(gp_output) == 1 else 9999999
    
class FitnessFunction1_2_E(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        expected_result = gp_input[0] * gp_input[1]
        return abs(gp_output[0] - expected_result) if len(gp_output) == 1 else 9999999
    
class FitnessFunction1_3_A(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        expected_result = max(gp_input[:2])
        return abs(gp_output[0] - expected_result) if len(gp_output) == 1 else 9999999
    
class FitnessFunction1_3_B(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        expected_result = max(gp_input[:2])
        return abs(gp_output[0] - expected_result) if len(gp_output) == 1 else 9999999
    
class FitnessFunction1_4_A(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        expected_result = int(sum(gp_input[:10]) / 10)
        return abs(gp_output[0] - expected_result) if len(gp_output) == 1 else 9999999
    
class FitnessFunction1_4_B(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        inputs = gp_input[0]
        expected_result = int(sum(gp_input[1:inputs + 1]) / inputs)
        return abs(gp_output[0] - expected_result) if len(gp_output) == 1 else 9999999
    
class FitnessFunctionB_1(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        float_to_add = gp_input[1] + (gp_input[2] / 10 ** len(str(gp_input[2])))
        expected_result = gp_input[0] + float_to_add
        return abs(gp_output[0] - expected_result) if len(gp_output) == 1 else 9999999
        
class FitnessFunctionB_21(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        expected_result = tuple(x if x >= 0 else 0 for x in gp_input)
        return sum(abs(o - e) for o, e in zip(gp_output, expected_result)) if len(gp_output) == len(expected_result) else 9999999
    
class FitnessFunctionB_28(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        expected_result = min(gp_input)
        return abs(gp_output[0] - expected_result) if len(gp_output) == 1 else 9999999
    
def get_fitness_function_by_name(name: str) -> Callable:
    return {
        '1.1.A': FitnessFunction1_1_A,
        '1.1.B': FitnessFunction1_1_B,
        '1.1.C': FitnessFunction1_1_C,
        '1.1.D': FitnessFunction1_1_D,
        '1.1.E': FitnessFunction1_1_E,
        '1.1.F': FitnessFunction1_1_F,
        '1.2.A': FitnessFunction1_2_A,
        '1.2.B': FitnessFunction1_2_B,
        '1.2.C': FitnessFunction1_2_C,
        '1.2.D': FitnessFunction1_2_D,
        '1.2.E': FitnessFunction1_2_E,
        '1.3.A': FitnessFunction1_3_A,
        '1.3.B': FitnessFunction1_3_B,
        '1.4.A': FitnessFunction1_4_A,
        '1.4.B': FitnessFunction1_4_B,
        'B.1': FitnessFunctionB_1,
        'B.21': FitnessFunctionB_21,
        'B.28': FitnessFunctionB_28,
    }[name]

def get_fitness_function(name: str) -> FitnessFunctionBase:
    return get_fitness_function_by_name(name)()

def generate_truth_tables(k: int) -> Tuple[Tuple[bool, ...], ...]:
    return tuple(product((True, False), repeat=k))

with open("grammar/src/genetic/evaluation/truth_tables.py", "w") as file:
    print("from typing import Tuple", file=file)
    print("", file=file)
    for k in range(1, 11):
        print(f"truth_table_{k} = Tuple[Tuple[int, ...], ...]", file=file)
    print("", file=file)
    for k in range(1, 11):
        print(f"truth_table_{k} = {generate_truth_tables(k)}", file=file)


def generate_input_values(values_range: Tuple[int, int]) -> Tuple[Tuple[int, int]]:
    return tuple(product(range(values_range[0], values_range[1] + 1), repeat=2))
