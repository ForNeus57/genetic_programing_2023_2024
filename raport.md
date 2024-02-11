# Programowanie genetyczne - raport końcowy

Autorzy: Dominik Breksa, Kaja Dzielnicka

[Funkcja dopasowania](#funkcja-dopasowania) 

[Przkładowe zadania testowe](#przykładowe-zadania-testowe)\
    [1.1.A](#11a) | 
    [1.1.B](#11b) | 
    [1.1.C](#11c) | 
    [1.1.D](#11d) | 
    [1.1.E](#11e) | 
    [1.1.F](#11f) | 
    [1.2.A](#12a) | 
    [1.2.B](#12b) | 
    [1.2.C](#12c) | 
    [1.2.D](#12d) | 
    [1.2.E](#12e) | 
    [1.3.A](#13a) | 
    [1.3.B](#13b) | 
    [1.4.A](#14a) | 
    [1.4.B](#14b) 

[Finealne testy systemu](#finealne-testy-systemu) \
    [Benchmarki](#benchmarki) | 
    [Regresja symboliczna dla funkcji boolowskiej](#regresja-symboliczna-dla-funkcji-boolowskiej)

## Funkcja dopasowania
```python
class FitnessFunctionBase(ABC):
    def convert_output(self, gp_output: Union[Tuple[int, ...], Tuple[float, ...], Tuple[bool, ...], None]) -> Tuple[int, ...]:
        if gp_output is None:
            return tuple()
        return tuple(int(x) if not isinstance(x, bool) else int(x) for x in gp_output)
    
    def calculate_fitness(self, gp_output: Union[Tuple[int, ...], Tuple[float, ...], Tuple[bool, ...], None], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        if gp_output is None or len(gp_output) == 0: 
            return 100000
        converted_output = self.convert_output(gp_output)
        return self._calculate_fitness_impl(converted_output, gp_input)
    
    @abstractmethod
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        pass
```

Jest to klasa bazowa dla funkcji dopasowania. Funkcja `convert_output` służy do konwersji wyniku zwracanego przez program genetyczny na krotkę liczb całkowitych. Funkcja `calculate_fitness` służy do obliczenia wartości funkcji dopasowania na podstawie wyniku programu genetycznego. Funkcja `_calculate_fitness_impl` jest funkcją abstrakcyjną, która musi być zaimplementowana w klasach dziedziczących. 


## Przykładowe zadania testowe
### 1.1.A
Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 1. Poza liczbą 1 może też zwrócić inne liczby.

- funkcja dopasowania:
```python
class FitnessFunction1_1_A(FitnessFunctionBase):
    def _calculate_fitness_impl(self, gp_output: Tuple[int, ...], gp_input: Optional[Tuple[int, ...]] = None) -> int:
        closest_value = min(gp_output, key=lambda x: abs(x - 1))
        return abs(closest_value - 1) if 1 not in gp_output else 0
```

- najlepsze rozwiązanie:
```
{
	while (false) {
		if (true) {
			write(0);
			read(c2);
			c2 = (c2 * c2);
			RYbi = 51;
		} else {
			read(Xqg);
			read(Xqg);
			Qig2X = 24;
			read(Xqg);
		}
		HnH = ((1 - -7) + (61 / 44));
		HnH = -39;
		while (true) {
			read(HnH);
			z5A = (HnH + -46);
		}
	}
	while (!((5 == 27))) {
		if (((29 / 32) <= (20 / -8))) {
			read(QF);
			eSl = 63;
			eSl = (QF - -38);
			hp = (eSl - -36);
		} else {
			I3Z = 19;
			I3Z = I3Z;
			I3Z = -9;
			nhms = (22 - I3Z);
		}
		uDVk = ((40 * 57) / -64);
		read(uDVk);
		write((uDVk * uDVk));
	}
}
```



### 1.1.B 
Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 789. Poza liczbą 789 może też zwrócić inne liczby.

### 1.1.C 
Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 31415. Poza liczbą 31415 może też zwrócić inne liczby.

### 1.1.D 
Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1. Poza liczbą 1 może też zwrócić inne liczby.

### 1.1.E 
Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 789. Poza liczbą 789 może też zwrócić inne liczby.

### 1.1.F 
Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę 1. Poza liczbą 1 NIE powinien nic więcej wygenerować.

### 1.2.A 
Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]

### 1.2.B 
Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9]

### 1.2.C 
Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]

### 1.2.D 
Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich różnicę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]

### 1.2.E 
Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich iloczyn. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]

### 1.3.A 
Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) większą z nich. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]

### 1.3.B 
Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) większą z nich. Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999]

### 1.4.A 
Program powinien odczytać dziesięć pierwszych liczy z wejścia i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną (zaokrągloną do pełnej liczby całkowitej). Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99]

### 1.4.B 
Program powinien odczytać na początek z wejścia pierwszą liczbę (ma być to wartość nieujemna) a następnie tyle liczb (całkowitych) jaka jest wartość pierwszej odczytanej liczby i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną zaokrągloną do pełnej liczby całkowitej (do średniej nie jest wliczana pierwsza odczytana liczba, która mówi z ilu liczb chcemy obliczyć średnią). Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99], pierwsza liczba może być tylko w zakresie [0,99].


## Finealne testy systemu

### Benchmarki
#### 1. Number IO 
Given an integer and a float, print their sum. 

#### 21. Negative To Zero
Given a vector of integers, return the vector where all negative integers have been replaced by 0.

#### 28. Smallest
Given four integers, print the smallest of them.



### Regresja symboliczna dla funkcji boolowskiej
