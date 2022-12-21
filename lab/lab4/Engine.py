class Engine:

    power: int = 100
    company: str

    def __init__(self, company: str, power: int) -> None:
        self.company = company
        self.power = power

    @staticmethod
    def car_start() -> None:
        print('Поехали')

    @staticmethod
    def car_stop() -> None:
        print('Останавливаемся')

    def __str__(self) -> str:
        return f'Мотор производства "{self.company}" с мощностью {self.power} л.с.'
