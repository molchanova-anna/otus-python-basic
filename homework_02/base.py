from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

"""доработайте базовый класс base.Vehicle:
добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
добавьте инициализатор для установки weight, fuel, fuel_consumption
добавьте метод start, который, если ещё не состояние started, проверяет, что топлива больше нуля, 
и обновляет состояние started, иначе выкидывает исключение exceptions.LowFuelError
добавьте метод move, который проверяет, что достаточно топлива для преодоления переданной дистанции, 
и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions.NotEnoughFuel"""


class Vehicle:
    weight: float = 750
    started: bool = False
    fuel: float = 10
    fuel_consumption: float = 0.075

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance: float):
        need_fuel = distance * self.fuel_consumption
        if self.fuel < need_fuel:
            raise NotEnoughFuel
        else:
            self.fuel -= need_fuel
