from typing import Any, Optional


class Node:
    """ Класс, который описывает узел двусвязного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None, prev_: Optional["Node"] = None):
        """
        Создаем новый узел для двусвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        self.next = None
        self.next = None
        self.set_next(next_)
        self.set_prev(prev_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        """
        Проверяет корректность узла.
        :param node: Узел для проверки
        :raises TypeError: Если узел некорректного типа
        """
        if not isinstance(node, (Node, type(None))):
            raise TypeError(f"Некорректный тип узла: ожидался 'Node' или 'None', получен {type(node).__name__}")

    def set_next(self, next_: Optional["Node"] = None) -> None:
        """
        Устанавливает следующий узел, проверяя его корректность.
        :param next_: Следующий узел или None
        """
        self.is_valid(next_)
        self.next = next_

    def set_prev(self, prev_: Optional["Node"] = None) -> None:
        """
        Устанавливает предыдущий узел, проверяя его корректность.
        :param prev_: Предыдущий узел или None
        """
        self.is_valid(prev_)
        self.prev = prev_

    def get_value(self) -> Any:
        """Метод, который возвращает значение атрибута value"""
        return self.value

    def get_next(self):
        """Метод, который возвращает значение атрибута next"""
        return self.next

    def get_prev(self):
        """Метод, который возвращает значение атрибута prev"""
        return self.prev
