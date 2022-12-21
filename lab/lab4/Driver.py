def fullname_driver(surname, name, middle_name):
    fullname = surname.capitalize() + ' ' + name.capitalize() + ' ' + middle_name.capitalize()
    return fullname


class Driver:
    surname: str
    name: str
    middle_name: str
    experience: int = 0

    def __init__(self, surname: str, name: str, middle_name: str, experience: int) -> None:
        self.surname = surname.strip()
        self.name = name.strip()
        self.middle_name = middle_name.strip()
        self.experience = experience

    def driver_turn_right(self) -> None:
        print(f'{fullname_driver(self.surname, self.name, self.middle_name)}, поворот направо!')

    def driver_turn_left(self) -> None:
        print(f'{fullname_driver(self.surname, self.name, self.middle_name)}, поворот налево')

    @property
    def word_selection_for_experience(self):

        match self.experience:
            case 1:
                return 'год'
            case 2 | 3 | 4:
                return 'года'
            case _:
                return 'лет'

    def __str__(self) -> str:
        return (f'Стаж вождения водителя {fullname_driver(self.surname, self.name, self.middle_name)}'\
                f' составляет {self.experience} {self.word_selection_for_experience}.')
