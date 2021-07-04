"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int = 1000

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super(Plane, self).__init__(weight=weight,
                                      fuel=fuel,
                                      fuel_consumption=fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo: int):
        new_cargo = self.cargo + add_cargo
        if new_cargo > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo = new_cargo

    def remove_all_cargo(self) -> int:
        prior_cargo = self.cargo
        self.cargo = 0
        return prior_cargo
