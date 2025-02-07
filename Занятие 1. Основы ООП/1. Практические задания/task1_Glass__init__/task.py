from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        # TODO создайте атрибут capacity_volume и occupied_volume Обязательно проверяйте типы (TypeError) и значения передаваемых аргументов (ValueError)
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if not capacity_volume > 0:
            raise ValueError("Объем стакана должен быть больше 0")
        self.capacity_volume = capacity_volume  # объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if occupied_volume < 0:
            raise ValueError("Не должно быть отрицательных значений")
        if occupied_volume > capacity_volume:
            raise ValueError("Налить в стакан больше того, что возможно нельзя")

        self.occupied_volume = occupied_volume  # о


if __name__ == "__main__":
    glass1 = Glass (300,250)
    glass2 = Glass (300,100)

    try:
        Glass(-11.5,400)  # TODO инициализировать не корректные объекты
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")


