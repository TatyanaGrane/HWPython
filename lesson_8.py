# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». # В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
from datetime import date
class Date:
    def __init__(self, d):
        self.d = d

    @classmethod
    def m_c(cls, d):
        return f"Число: {int(d[0:2])}; тип: {type(int(d[0:2]))}\n" \
               f"Месяц: {int(d[3:5])}; тип: {type(int(d[3:5]))}\n" \
               f"Год: {int(d[6:])}; тип: {type(int(d[6:]))}"

    @staticmethod
    def m_s(self):
        if int(self.d[0:2]) <= 31 and int(self.d[3:5]) <= 12 and int(self.d[6:]) <= 2021:
            return f"Date is correct: {int(self.d[0:2])}-{int(self.d[3:5])}-{int(self.d[6:])}"
        else:
            print("Incorrect date!")

our_date = date.today()
correct_date = our_date.strftime("%d-%m-%Y")
x = Date(correct_date)
print(x.m_c(correct_date))
print(x.m_s(x))


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.
class MyExc(Exception):
    def __init__(self, a):
        self.a = a

    def __truediv__(self, other):
        if other.a != 0:
            return round(self.a / other.a)
        else:
            other.a = int(input("Error! Enter number 2 > 0: "))
            return round(self.a / other.a)

first = MyExc(int(input("Enter number 1: ")))
second = MyExc(int(input("Enter number 2: ")))
print(first / second)

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class NewExc(Exception):
    my_list = []
    while True:
        a = input("Enter numbers for continue or 'stop' for exit: ")
        if a == 'stop':
            print(f"Final list: {my_list}")
            break
        try:
            if not a.isnumeric():
                raise ValueError
            my_list.append(int(a))
        except ValueError as error:
            print("Only numbers!")

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.
class Warehouse:
    def __init__(self):
        self.w_dict = {}

    def add_to(self, equipment):
       self.w_dict.setdefault(equipment.group_name(), []).append(equipment)

class Equipment:
    def __init__(self, name, year, count):
        self.name = name
        self.year = year
        self.count = count
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.year} {self.count}'

class Printer(Equipment):
    def __init__(self, name, year, count, color):
        super().__init__(name, year, count)
        self.color = color

    def __repr__(self):
        return f'{self.name} {self.year} {self.count} {self.color}'

class Scan(Equipment):
    def __init__(self, name, year, count, model):
        super().__init__(name, year, count)
        self.model = model

    def __repr__(self):
        return f'{self.name} {self.year} {self.count} {self.model}'

class Xerox(Equipment):
    def __init__(self, name, year, count, speed):
        super().__init__(name, year, count)
        self.speed = speed

    def __repr__(self):
        return f'{self.name} {self.year} {self.count} {self.speed}'

sklad = Warehouse()
i = 0
while True:
    if input("Введите 'A' для завершения. Нажмите 'Enter' для продолжения: ").upper() == 'A':
        break
    enter = input("For add printer enter 'p', scan - 's', xerox - 'x': ")
    if enter == 'p':
        pr_name = input("Enter name printer: ")
        pr_year = input("Enter year printer: ")
        try:
            int(pr_year)
        except ValueError:
            pr_year = int(input("Only numbers! Enter year printer: "))
        pr_count = input("Enter count printer: ")
        try:
            int(pr_count)
        except ValueError:
            pr_count = input("Only numbers! Enter count printer: ")
        pr_color = input("Enter color printer: ")
        a = Printer(pr_name, pr_year, pr_count, pr_color)
        sklad.add_to(a)

    elif enter == 's':
        sc_name = input("Enter name scan: ")
        sc_year = input("Enter year scan: ")
        try:
            int(sc_year)
        except ValueError:
            sc_year = int(input("Only numbers! Enter year scan: "))
        sc_count = input("Enter count scan: ")
        try:
            int(sc_count)
        except ValueError:
            sc_count = input("Only numbers! Enter count scan: ")
        sc_model = input("Enter model scan: ")
        b = Scan(sc_name, sc_year, sc_count, sc_model)
        sklad.add_to(b)

    elif enter == 'x':
        x_name = input("Enter name xerox: ")
        x_year = input("Enter year xerox: ")
        try:
            int(x_year)
        except ValueError:
            x_year = int(input("Only numbers! Enter year xerox: "))
        x_count = input("Enter count xerox: ")
        try:
            int(x_count)
        except ValueError:
            x_count = int(input("Only numbers! Enter count xerox: "))
        x_speed = input("Enter speed xerox: ")
        try:
            int(x_speed)
        except ValueError:
            x_speed = int(input("Only numbers! Enter speed xerox: "))
        c = Xerox(x_name, x_year, x_count, x_speed)
        sklad.add_to(c)
print(sklad.w_dict)

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
class ComplexNum:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __mul__(self, other):
        return self.x * other.x

a = ComplexNum(1+2j)
b = ComplexNum(4+5j)
print(f"Sum a, b: {a + b}")
print(f"Multiplex a, b: {a * b}")