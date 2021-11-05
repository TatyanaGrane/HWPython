# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
with open("f_5_1.txt", "a", encoding="utf-8") as f:
    while True:
        data = input("Enter data or press 'Enter' to done: ")
        f.write(f"{data}\n")
        if not data:
            break


# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк
# и слов в каждой строке.
with open("f_5_2", "r", encoding="utf-8") as f2:
    line = f2.readline().split()
    while line:
        print(f"Строка {line} содержит {len(line)} слов.")
        line = f2.readline().split()
    f2.seek(0)
    print(f"Всего строк: {len(f2.readlines())}.")

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
with open("text_3.txt", "r", encoding="utf-8") as f3:
    print("Имеют зарплату меньше 20 тысяч рублей: ")
    line = f3.readline().split()
    while line:
        if float(line[1]) < 20000.0:
            float(line[1])
            print(f"Фамилия: {line[0]}, зарплата: {line[1]}")
            line = f3.readline().split()
        else:
            line = f3.readline().split()

with open("text_3.txt", "r", encoding="utf-8") as f3:
    lines = f3.read().split()
    # print(lines)
    a = 0
    salary = 0.0
    for i in lines:
        if lines.index(i) % 2 == 1:
            salary += float(i)
            # cs = salary
            a += 1
    print(f"Средняя величина дохода сотрудников: {salary / a}")

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
ru_list = []
with open("text_4.txt", "r", encoding="utf-8") as f4:
    line = f4.readline().split()
    line[0] = "Один"
    line[2] = "1\n"
    str_1 = ' '.join(line)
    ru_list.append(str_1)
    line = f4.readline().split()
    line[0] = "Два"
    line[2] = "2\n"
    str_2 = ' '.join(line)
    ru_list.append(str_2)
    line = f4.readline().split()
    line[0] = "Три"
    line[2] = "3\n"
    str_3 = ' '.join(line)
    ru_list.append(str_3)
    line = f4.readline().split()
    line[0] = "Четыре"
    line[2] = "4\n"
    str_4 = ' '.join(line)
    ru_list.append(str_4)
    with open("text_4_ru.txt", "w", encoding="utf-8") as f4_ru:
        f4_ru.write(''.join(ru_list))

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from functools import reduce
from random import randint
with open("f_5_5.txt", "w", encoding="utf-8") as f5:
    new_list = [randint(0, 10) for el in range(10)]
    str_list = ''
    for i in new_list:
        i = str(i)
        str_list += i
    f5.write(f"Набор чисел: {' '.join(str_list)}")
    def sum_func(el1, el2):
        return el1 + el2
    f5.write(f"\nСумма числе равна {str(reduce(sum_func, new_list))}")

# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет
# и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
dict_6 = {}
with open("text_6.txt", "r", encoding="utf-8") as f6:
    for i in f6:
        key, hours = i.split(':')
        key_sum = sum(map(int, "".join([_ for _ in hours if _ == ' ' or '9' >= _ >= '0']).split()))
        dict_6[key] = key_sum
print(dict_6)

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

with open("f7.json", "w", encoding="utf-8") as f7_json:
    with open("text_7.txt", "r", encoding="utf-8") as f7:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f7}
        result = [profit, {"Average profit:": round(sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, f7_json, ensure_ascii=False, indent=4)