# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.
from time import sleep
class TrafficLight:
    __color = "nothing"

    def running(self):
        while True:
            print("Current color is red.")
            sleep(7)
            print("Current color is yellow.")
            sleep(2)
            print("Current color is green.")
            sleep(10)
            print("Current color is yellow.")
            sleep(2)


light_1 = TrafficLight()
light_1.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    _length = 1000
    _width = 20

    def square(self, l, w):
        self._length = l
        self._width = w
        return l, w


class Asphalt(Road):                             # Можно ли было решить таким способом?

    def asphalt_mass(self, l, w, m=25, t=5):
        super().square(l, w)
        self.mass_km_cm = m
        self. thickness = t
        return l * w * m * t
road_1 = Asphalt()

print(f"Необходимая для покрытия всего дорожного полотна размерами 20 на 5000 масса асфальта: {int(road_1.asphalt_mass(20, 5000) / 1000)} тонн.")


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Name: {self.name}\nSurname: {self.surname}")

    def get_total_income(self):
        print(f'Position: {self.position}\nTotal income: {self._income.get("wage") + self._income.get("bonus")}')


employee = Position("Ivan", "Ivanov", "analyst", 150000, 25000)
employee.get_full_name()
employee.get_total_income()

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    speed = 0
    color = "color"
    name = "Name"
    is_police = False

    def go(self):
        print(f"{self.name} started moving.")

    def stop(self):
        print(f"{self.name} stopped.")

    def turn(self, side):
        self.direction = side
        print(f"{self.name} turned {side}.")

    def show_speed(self, s):
        self.speed = s
        print(f"Current speed of {self.name}: {s} km/h.")

class TownCar(Car):
    def show_speed(self, s_c):
        Car.speed = s_c
        if s_c > 60:
            print(f"Speed was exceeded, current speed: {s_c}")
        else:
            print(f"Current speed: {s_c} km/h.")
class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self, s_c):
        Car.speed = s_c
        if s_c > 40:
            print(f"Speed was exceeded, current speed: {s_c}")
        else:
            print(f"Current speed: {s_c} km/h.")

class PoliceCar(Car):
    pass

car_town = TownCar()
car_town.name = "Bentley"
print(f"Name of town car is {car_town.name}")
car_town.color = "red"
print(f"Color of town car is {car_town.color}")
car_town.is_police = False
print(f"Town car is police car: {car_town.is_police}")
car_town.go()
car_town.stop()
car_town.turn("left")
car_town.show_speed(80)

car_sport = SportCar()
car_sport.name = "Ferrari"
print(f"Name of sport car is {car_sport.name}")
car_sport.color = "yellow"
print(f"Color of sport car is {car_sport.color}")
car_sport.is_police = False
print(f"Town car is  police car: {car_sport.is_police}")
car_sport.go()
car_sport.stop()
car_sport.turn("right")
car_sport.show_speed(180)

car_work = WorkCar()
car_work.name = "Ford"
print(f"Name of sport car is {car_work.name}")
car_work.color = "metallic"
print(f"Color of sport car is {car_work.color}")
car_work.is_police = False
print(f"Town car is  police car: {car_work.is_police}")
car_work.go()
car_work.stop()
car_work.turn("right")
car_work.show_speed(45)

car_police = PoliceCar()
car_police.name = "Lada"
print(f"Name of police car is {car_police.name}")
car_police.color = "white"
print(f"Color of police car is {car_police.color}")
car_police.is_police = True
print(f"Town car is  police car: {car_police.is_police}")
car_police.go()
car_police.stop()
car_police.turn("left")
car_police.show_speed(60)

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. 
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = "name"

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с помощью атрибута '{self.title}'.")

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с помощью атрибута '{self.title}'.")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с помощью атрибута '{self.title}'.")

stationery = Stationery()
stationery.draw()
pen = Pen()
pen.title = "ручка"
print(f"Канцелярская принадлежность: {pen.title}.")
pen.draw()
pencil = Pencil()
pencil.title = "карандаш"
print(f"Канцелярская принадлежность: {pencil.title}.")
pencil.draw()
handle = Handle()
handle.title = "маркер"
print(f"Канцелярская принадлежность: {handle.title}.")
handle.draw()

