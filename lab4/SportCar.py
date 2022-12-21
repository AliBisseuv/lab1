from Car import Car


class SportCar(Car):
    max_speed: float

    def __init__(self, max_speed: float, **kwargs) -> None:
        self.max_speed = max_speed
        super().__init__(**kwargs)

    def __str__(self) -> str:
        print(super().__str__())
        return f'Максимальная скорость составляет {str(self.max_speed)} км/ч.'
