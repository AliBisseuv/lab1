from Car import Car, word_selection_for_weight


class Lorry(Car):
    carrying: float

    def __init__(self, carrying: float, **kwargs) -> None:
        self.carrying = carrying
        super().__init__(**kwargs)

    def __str__(self) -> str:
        print(super().__str__())
        return f'Максимальная грузоподъемность составляет {str(self.carrying)} ' \
               f'{word_selection_for_weight(self.carrying)}.'


# lr = Lorry(carrying=35, surname='бисеув', name='али', middle_name='курмангалиевич', power=120, company='ЗИЛ',
#            car_class='грузовой', mark='ЗИЛ-130', weight=3521, experience=21)
# print(lr)
