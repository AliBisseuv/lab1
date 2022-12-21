from Driver import Driver


class Person(Driver):
    ful_name: Driver
    age: int

    def __init__(self, age: int, **kwargs) -> None:
        self.age = age
        super().__init__(**kwargs)

    def __str__(self) -> str:
        print(super().__str__())
        return f'Его возраст составляет {str(self.age)} {self.experience}'
