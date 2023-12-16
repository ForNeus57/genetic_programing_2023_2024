import numpy as np


# f(x) = 5x^3 -2x^2 + 3x - 17
def f1(x):
    return 5 * x ** 3 - 2 * x ** 2 + 3 * x - 17


# f(x) = sin(x) + cos(x)
def f2(x):
    return np.sin(x) + np.cos(x)


# f(x) = 2 * ln(x+1)
def f3(x):
    return 2 * np.log(x + 1)


# f(x, y) = x + 2y
def f4(x, y):
    return x + 2 * y


# f(x, y) = sin(x/2) + 3cos(x)
def f5(x, y):
    return np.sin(x / 2) + 3 * np.cos(y)


# f(x, y) = x^2 + 3xy - 7y + 1
def f6(x, y):
    return x ** 2 + 3 * x * y - 7 * y + 1


def f7(x: np.ndarray) -> np.ndarray:
    """
    f(x) = sin(x + pi/2)
    """
    return np.sin(x + np.pi / 2)


def f8(x: np.ndarray) -> np.ndarray:
    """
    f(x) = tan(2x + 1)
    """
    return np.tan(2 * x + 1)


def create_file1000(file_name, numbers, results):
    file = open(file_name, "w")
    file.write("1 100 -5 5 1000\n")
    for i in range(len(numbers)):
        file.write(str(numbers[i]) + " " + str(results[i]) + "\n")
    file.close()


def create_file2000(file_name, numbers, results):
    file = open(file_name, "w")
    file.write("1 100 -5 5 2000\n")
    for i in range(len(numbers)):
        file.write(str(numbers[i]) + " " + str(results[i]) + "\n")
    file.close()


def create_file3000(file_name, numbers, results):
    file = open(file_name, "w")
    file.write("1 100 -5 5 3000\n")
    for i in range(len(numbers)):
        file.write(str(numbers[i]) + " " + str(results[i]) + "\n")
    file.close()


def create_file4000(file_name, numbers, results):
    file = open(file_name, "w")
    file.write("1 100 -5 5 4000\n")
    for i in range(len(numbers)):
        file.write(str(numbers[i]) + " " + str(results[i]) + "\n")
    file.close()


def create_file5000(file_name, numbers, results):
    file = open(file_name, "w")
    file.write("1 100 -5 5 5000\n")
    for i in range(len(numbers)):
        file.write(str(numbers[i]) + " " + str(results[i]) + "\n")
    file.close()


def create_file_fxy_1000(file_name, numbers_x, numbers_y, results):
    file = open(file_name, "w")
    file.write("2 100 -5 5 1000\n")
    for i in range(len(numbers_x)):
        file.write(str(numbers_x[i]) + " " + str(numbers_y[i]) + " " + str(results[i]) + "\n")
    file.close()


def create_file_fxy_2000(file_name, numbers_x, numbers_y, results):
    file = open(file_name, "w")
    file.write("2 100 -5 5 2000\n")
    for i in range(len(numbers_x)):
        file.write(str(numbers_x[i]) + " " + str(numbers_y[i]) + " " + str(results[i]) + "\n")
    file.close()


def create_file_fxy_3000(file_name, numbers_x, numbers_y, results):
    file = open(file_name, "w")
    file.write("2 100 -5 5 3000\n")
    for i in range(len(numbers_x)):
        file.write(str(numbers_x[i]) + " " + str(numbers_y[i]) + " " + str(results[i]) + "\n")
    file.close()


def create_file_fxy_4000(file_name, numbers_x, numbers_y, results):
    file = open(file_name, "w")
    file.write("2 100 -5 5 4000\n")
    for i in range(len(numbers_x)):
        file.write(str(numbers_x[i]) + " " + str(numbers_y[i]) + " " + str(results[i]) + "\n")
    file.close()


def create_file_fxy_5000(file_name, numbers_x, numbers_y, results):
    file = open(file_name, "w")
    file.write("2 100 -5 5 5000\n")
    for i in range(len(numbers_x)):
        file.write(str(numbers_x[i]) + " " + str(numbers_y[i]) + " " + str(results[i]) + "\n")
    file.close()


# # f1 dla dziedziny <-10, 10>
# # 1000 punktów o równych odstępach
# x = np.linspace(-10, 10, 1000)
# y = f1(x)
# create_file1000("1_1.dat", x, y)
#
# # f1 dla dziedziny <0, 100>
# # 2000 punktów o równych odstępach
# x = np.linspace(0, 100, 2000)
# y = f1(x)
# create_file2000("1_2.dat", x, y)
#
# # f1 dla dziedziny <-1, 1>
# # 1000 punktów o równych odstępach
# x = np.linspace(-1, 1, 1000)
# y = f1(x)
# create_file1000("1_3.dat", x, y)
#
# # f1 dla dziedziny <-1000, 1000>
# # 5000 punktów o równych odstępach
# x = np.linspace(-1000, 1000, 5000)
# y = f1(x)
# create_file5000("1_4.dat", x, y)
#
# # f2 dla dziedziny <-3.14, 3.14>
# # 1000 punktów o równych odstępach
# x = np.linspace(-3.14, 3.14, 1000)
# y = f2(x)
# create_file1000("2_1.dat", x, y)
#
# # f2 dla dziedziny <0, 7>
# # 1000 punktów o równych odstępach
# x = np.linspace(0, 7, 1000)
# y = f2(x)
# create_file1000("2_2.dat", x, y)
#
# # f2 dla dziedziny <0, 100>
# # 2000 punktów o równych odstępach
# x = np.linspace(0, 100, 2000)
# y = f2(x)
# create_file2000("2_3.dat", x, y)
#
# # f2 dla dziedziny <-100, 100>
# # 3000 punktów o równych odstępach
# x = np.linspace(-100, 100, 3000)
# y = f2(x)
# create_file3000("2_4.dat", x, y)
#
# # f3 dla dziedziny <0, 4>
# # 1000 punktów o równych odstępach
# x = np.linspace(0, 4, 1000)
# y = f3(x)
# create_file1000("3_1.dat", x, y)
#
# # f3 dla dziedziny <0, 9>
# # 1000 punktów o równych odstępach
# x = np.linspace(0, 9, 1000)
# y = f3(x)
# create_file1000("3_2.dat", x, y)
#
# # f3 dla dziedziny <0, 99>
# # 2000 punktów o równych odstępach
# x = np.linspace(0, 99, 2000)
# y = f3(x)
# create_file2000("3_3.dat", x, y)
#
# # f3 dla dziedziny <0, 999>
# # 3000 punktów o równych odstępach
# x = np.linspace(0, 999, 3000)
# y = f3(x)
# create_file3000("3_4.dat", x, y)
#
# # f4 dla dziedziny <0, 1>
# # 1000 punktów o równych odstępach
# x = np.linspace(0, 1, 1000)
# y = np.linspace(0, 1, 1000)
# np.random.shuffle(y)
# z = f4(x, y)
# create_file_fxy_1000("4_1.dat", x, y, z)
#
# # f4 dla dziedziny <-10, 10>
# # 1000 punktów o równych odstępach
# x = np.linspace(-10, 10, 1000)
# y = np.linspace(-10, 10, 1000)
# np.random.shuffle(y)
# z = f4(x, y)
# create_file_fxy_1000("4_2.dat", x, y, z)
#
# # f4 dla dziedziny <0, 100>
# # 2000 punktów o równych odstępach
# x = np.linspace(0, 100, 2000)
# y = np.linspace(0, 100, 2000)
# np.random.shuffle(y)
# z = f4(x, y)
# create_file_fxy_2000("4_3.dat", x, y, z)
#
# # f4 dla dziedziny <-1000, 1000>
# # 4000 punktów o równych odstępach
# x = np.linspace(-1000, 1000, 4000)
# y = np.linspace(-1000, 1000, 4000)
# np.random.shuffle(y)
# z = f4(x, y)
# create_file_fxy_4000("4_4.dat", x, y, z)
#
# # f5 dla dziedziny <-3.14, 3.14>
# # 1000 punktów o równych odstępach
# x = np.linspace(-3.14, 3.14, 1000)
# y = np.linspace(-3.14, 3.14, 1000)
# np.random.shuffle(y)
# z = f5(x, y)
# create_file_fxy_1000("5_1.dat", x, y, z)
#
# # f5 dla dziedziny <0, 7>
# # 1000 punktów o równych odstępach
# x = np.linspace(0, 7, 1000)
# y = np.linspace(0, 7, 1000)
# np.random.shuffle(y)
# z = f5(x, y)
# create_file_fxy_1000("5_2.dat", x, y, z)
#
# # f5 dla dziedziny <0, 100>
# # 2000 punktów o równych odstępach
# x = np.linspace(0, 100, 2000)
# y = np.linspace(0, 100, 2000)
# np.random.shuffle(y)
# z = f5(x, y)
# create_file_fxy_2000("5_3.dat", x, y, z)
#
# # f5 dla dziedziny <-100, 100>
# # 3000 punktów o równych odstępach
# x = np.linspace(-100, 100, 3000)
# y = np.linspace(-100, 100, 3000)
# np.random.shuffle(y)
# z = f5(x, y)
# create_file_fxy_3000("5_4.dat", x, y, z)
#
# # f6 dla dziedziny <-10, 10>
# # 1000 punktów o równych odstępach
# x = np.linspace(-10, 10, 1000)
# y = np.linspace(-10, 10, 1000)
# np.random.shuffle(y)
# z = f6(x, y)
# create_file_fxy_1000("6_1.dat", x, y, z)
#
# # f6 dla dziedziny <0, 100>
# # 2000 punktów o równych odstępach
# x = np.linspace(0, 100, 2000)
# y = np.linspace(0, 100, 2000)
# np.random.shuffle(y)
# z = f6(x, y)
# create_file_fxy_2000("6_2.dat", x, y, z)
#
# # f6 dla dziedziny <-1, 1>
# # 1000 punktów o równych odstępach
# x = np.linspace(-1, 1, 1000)
# y = np.linspace(-1, 1, 1000)
# np.random.shuffle(y)
# z = f6(x, y)
# create_file_fxy_1000("6_3.dat", x, y, z)
#
# # f6 dla dziedziny <-1000, 1000>
# # 5000 punktów o równych odstępach
# x = np.linspace(-1000, 1000, 5000)
# y = np.linspace(-1000, 1000, 5000)
# np.random.shuffle(y)
# z = f6(x, y)
# create_file_fxy_5000("6_4.dat", x, y, z)

# f7 dla dziedziny < -pi, pi >
# 1000 punktów o równych odstępach
x = np.linspace(-np.pi, np.pi, 1000)
y = f7(x)
create_file1000("../../../data/7_1.dat", x, y)


# f8 dla diedziny < -pi, pi >
x = np.linspace(-np.pi, np.pi, 1000)
y = f8(x)
create_file1000("../../../data/8_1.dat", x, y)
