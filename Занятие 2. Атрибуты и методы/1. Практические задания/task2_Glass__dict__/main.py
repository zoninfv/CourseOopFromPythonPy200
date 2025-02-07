from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        print(self.__dict__)# TODO Распечатайте словарь атрибутов экземпляра класса в начале метода
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане
        print(self.__dict__)# TODO Распечатайте словарь атрибутов экземпляра класса в конце метода


if __name__ == "__main__":
    glass = Glass(200, 100)
