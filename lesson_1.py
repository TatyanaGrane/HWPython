# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
a = 5
b = 9
print(a*b)

print(a, b)
n = input("Enter first number: ")
h = input("Enter second number: ")
n = int(n)
h = int(h)
d = n + h
m = n - h
g = n * h
r = n / h
print("Sum: ", d)
print("Difference: ", m)
print("Multiplication: ", g)
print("Quotient: ", r)

z = input("Enter your name: ")
x = int(input("Enter your age: "))
print("Hello, user!")
print("Your name is ", z)
print("Age: ", x)

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input("Enter seconds: "))
h = seconds // 3600
m = (seconds % 3600) // 60
s = ((seconds % 3600) % 60)
print(f"Time: {h:02}:{m:02}:{s:02}")

#вариант 2:
# seconds = int(input("Enter seconds: "))
# print(f"Time: {seconds // 3600:02}:{(seconds % 3600) // 60:02}:{((seconds % 3600) % 60):02}")


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

t = input("Enter your number: ")
t1 = int(t)
t2 = int(t + t)
t3 = int(t + t + t)
sum_t = t1 + t2 + t3
print("Sum: ", sum_t)
# а если ввведет отрицательное значение?
while n < '0':
    print("Введите больше 0")


# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

x = int(input("Enter number: "))
a = x % 10
while x > 0:
    if x % 10 > a:
        a = x % 10
    x = x // 10
print(a)


# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
#
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

r = int(input("Enter revenue: "))
c = int(input("Enter costs: "))
if r > c:
    print("Profit: ", r - c)
    p = r - c
    print(f"Profitability: {100 * p / r:.1f}%")
    e = int(input("Enter number of employees: "))
    print(f"Profit per employee: {p / e:.3f}")
else:
    print("Loss: ", r - c)


# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

a = int(input("Enter first result: "))
b = int(input("Enter desired result: "))
d = 1
while a < b:
    d += 1
    a = a + 0.1 * a
print(d)