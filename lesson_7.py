 # 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 # который должен принимать данные (список списков) для формирования матрицы.
 # Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
 # Примеры матриц вы найдете в методичке.
 # Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
 # Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
 # Результатом сложения должна быть новая матрица.
 # Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
 # складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join([f"{i:02}" for i in line]) for line in self.matrix)

    def __add__(self, other):
        new_matrix = [[int(self.matrix[line][i]) + int(other.matrix[line][i]) for i in range(len(self.matrix[line]))] for line in range(len(self.matrix))]
        return new_matrix

matr_1 = [[1, 2], [3, 4]]
matr_2 = [[5, 6], [7, 8]]

m1 = Matrix(matr_1)
m2 = Matrix(matr_2)
c = Matrix(m1 + m2)
print(c)

 # 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
 # проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
 # У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
 # Это могут быть обычные числа: V и H, соответственно.
 # Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
 # для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
 # Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
 # реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

class Clothes(ABC):
    result = 0
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def material(self):
        pass

    def __add__(self, other):
        Clothes.result += self.material + other.material
        return f"Total value of material: {Clothes.result}"

class Coat(Clothes):
    @property
    def material(self):
        return round(self.param / 6.5 + 0.5)

class Suit(Clothes):
    @property
    def material(self):
        return round((self.param * 2 + 0.3) / 100)

coat = Coat(46)
print(f"Material for coat: {coat.material}")
suit = Suit(176)
print(f"Material fot suit: {suit.material}")
print(coat + suit)

# Вариант по разбору с урока с несколькими слогаемыми (больше 2)
from abc import ABC, abstractmethod

class Clothes(ABC):
    result = 0
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def material(self):
        pass

    def __add__(self, other):
        Clothes.result += self.material + other.material
        return Suit(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"

class Coat(Clothes):
    @property
    def material(self):
        return round(self.param / 6.5 + 0.5)

class Suit(Clothes):
    @property
    def material(self):
        return round((self.param * 2 + 0.3) / 100)

coat = Coat(46)
print(f"Material for coat: {coat.material}")
suit = Suit(176)
print(f"Material fot suit: {suit.material}")
print(f"Total value of material: {coat + suit + coat}")

 # 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
 # инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы
 # методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
 # деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
 # умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
 # округление значения до целого числа.
 # Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
 # Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
 # больше нуля, иначе выводить соответствующее сообщение.
 # Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
 # этих двух клеток.
 # Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
 # ячеек этих двух клеток.
 # В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
 # метод позволяет организовать ячейки по рядам.
 # Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
 # Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
 # Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
 # *****\n*****\n**.
 # Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
 # *****\n*****\n*****.
class Cell:
    # c = []
    def __init__(self, cell):
        self.cell = cell

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.cell // rows)]) + '\n' + '*' * (self.cell % rows)

    def __str__(self):
        return f"{self.cell}"

    def __add__(self, other):
        print("Сумма чисел ячеек клеток: ")
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        print("Разность чисел ячеек клеток: ")
        return Cell(self.cell - other.cell) if self.cell - other.cell > 0 \
            else "Число ячеек первой клетки меньше числа второй: вычитание невозможно."

    def __mul__(self, other):
        print("Произведение чисел ячеек клеток: ")
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        print("Частное чисел ячеек клеток: ")
        return Cell(self.cell // other.cell)

a = Cell(12)
b = Cell(13)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(f"Matrix of a:\n{a.make_order(5)}")
print(f"Matrix of b:\n{b.make_order(5)}")