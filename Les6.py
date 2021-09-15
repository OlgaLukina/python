1
from time import sleep

class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running (self):
        i=0
        while i<3:
            print (TrafficLight.__color[i])
            if i==0:
                sleep(7)
            elif i==1:
                sleep(5)
            elif i==2:
                sleep(7)
            i=i+1

light = TrafficLight()
light.running()

2
class Road:

    def __init__(self, _length, _width):
        self._length=_length
        self._width=_width

    def result (self):
        mass = 25
        thickness = 5
        return self._width * self._length * mass * thickness

road = Road (20, 5000)
print (road.result())

3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name=name
        self.surname=surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position (Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name+self.surname

    def get_total_income(self):
        return self._income

worker = Position ('Ivan', 'Petrov', 'work', 10000, 20000)
print (worker.get_full_name(), worker.get_total_income())

4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'машина поехала'
    def stop(self):
        return 'машина остановилась'
    def turn(self, direction):
        return (f'машина повернула {direction}')

class TownCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return 'превышение скорости'
        else:
            print (self.speed)

class SportCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'превышение скорости'
        else:
            print (self.speed)

class PoliceCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

lada = TownCar (100, 'red', 'lada', False)
mazda = SportCar (40, 'yellow', 'mazda', True)
ford = WorkCar (30, 'white', 'ford', False)
bmw = PoliceCar (50, 'black', 'bmw', True)

print(lada.show_speed())
print(mazda.turn('направо'))
print(ford.show_speed())
print(bmw.is_police)

5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Нарисовано ручкой'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Нарисовано карандашом'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Нарисовано маркером'

pen = Pen ('ручка')
pencil = Pencil ('карандаш')
handle = Handle ('маркер')

print(pen.draw())
print(pencil.draw())
print(handle.draw())