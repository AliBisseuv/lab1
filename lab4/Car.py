from Driver import Driver
from Engine import Engine


def word_selection_for_weight(value: float) -> str:
    weight_car_units = value - (value // 10) * 10
    match weight_car_units:
        case 1:
            return 'тонна'
        case 2 | 3 | 4:
            return 'тонны'
        case _:
            return 'тонн'


class Car:
    car_class: str
    mark: str
    weight: float = 1000
    engine: Engine
    driver: Driver

    def __init__(self, car_class, mark, weight, surname, name, middle_name, experience, company, power) -> None:
        self.driver = Driver(surname, name, middle_name, experience)
        self.engine = Engine(company, power)
        self.car_class = car_class
        self.mark = mark
        self.weight = weight

    def __str__(self) -> str:
        print(self.driver.__str__())
        print(self.engine.__str__())
        return f'Автомобилю марки "{self.mark}" относиться к классу "{self.car_class}" ' \
               f'с массой кузова {self.weight}  {word_selection_for_weight(self.weight)}.'
