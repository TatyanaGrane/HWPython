# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_f(a, b):
    try:
        a = int(a)
        b = int(b)
        c = a / b
    except ValueError:
        return "ValueError"
    except ZeroDivisionError as er:
        return er
    return round(c, 4)

print(my_f(a=input("Enter first number: "), b=input("Enter second number: ")))

# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
# -------------------------------------------Вариант 1---------------------------------------------------------------------
def my_f1():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    birth_year = input("Enter your birth year: ")
    city = input("Enter city where you live: ")
    email = input("Enter your email: ")
    mobile = input("Enter your mobile number: ")
    print(f"Your name - {name} {surname}. Year birth - {birth_year}. City - {city}. Email - {email}. Mobile - {mobile}.")

my_f1()

# -------------------------------------------Вариант 2---------------------------------------------------------------------
def my_f2(name = 'Ivan', surname = 'Ivanov', birth_year = '2000', city = 'Moscow', email = 'i.ivanov@example.com', mobile = '12345678900'):
    print(f"Your name - {name} {surname}. Year birth - {birth_year}. City - {city}. Email - {email}. Mobile - {mobile}.")
my_f2(name=input("Enter your name: "), surname=input("Enter your surname: "), birth_year=input("Enter your birth year: "), city=input("Enter city where you live: "), email=input("Enter your email: "), mobile=input("Enter your mobile number: "))

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
def my_func(x, y, z):
    if x is min(x, y, z):
        print(y + z)
    elif y is min(x, y, z):
        print(x + z)
    else:
        print(x + y)
my_func(x=int(input("Enter x: ")), y=int(input("Enter y: ")), z=int(input("Enter z: ")))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Возведение в степень с помощью оператора **
def step():
    x = float(input("Enter positive number: "))
    y = int(input("Enter negative number with '-': "))
    print(x ** y)
step()

# Реализация без оператора **, предусматривающая использование цикла
def step(x, y):
    a = 1
    for i in range(y):
        a = a * x
    return round((1 / a), 4)

print(step(x=abs(float(input("Enter positive number: "))), y=abs(int(input("Enter negative number: ")))))

# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

def sum_num():
    s = 0
    while True:
        numbers = input("Введите число, для завершения нажмите 'a': ") # При использовании .split() результат не складывает цифры,
        for i in numbers:                                               # складывает с ними только следующие вводы
            if i.lower() == "a":
                return s
            else:
                try:
                    s += int(i)
                except ValueError:
                    print("Для завершения нажмите 'a': ")
        print(f"Sum of numbers is {s}")

print(sum_num())

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func():
    words = input("Enter your word: ").lower()
    eng_let = 'abcdefghijklmopqrstuvwxyz'
    for i in words:
        if i in eng_let:
            return words.title()
        else:
            return "Only latin letters!"

print(int_func())

# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
def int_func():
    words = input("Enter your word: ").lower()
    eng_let = 'abcdefghijklmopqrstuvwxyz'
    for i in words:
        if i in eng_let:
            return words.title()
        else:
            return "Only latin letters!"

print(int_func())
# Комментарий от студента: Не поняла, чем отличаются 6 и 7 задания, если по коду 6-го работает и 7-е.