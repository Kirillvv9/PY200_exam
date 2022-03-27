from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self._value = value
        self._next = next_

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._value}, {self._next})"

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, prev: Optional["Node"] = None, next_: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self.is_valid(prev)
        self._prev = prev

    def __repr__(self):
        return f"{self.__class__.__name__}({self._prev}, {self._value}, {self._next})"

if __name__ == "__main__":
    ...

#  Сделать класс Node, который будет содержать в себе:
#  атрибуты:
    #  value
#  свойства:
    #  next
#  методы:
    #  __str__
    #  __repr__
    #  is_valid
#  Сделать DoubleLinkedNode наследуясь от класса Node
#  В конструкторе DoubleLinkedNode определить дополнительный атрибут prev,
#  хранящий в себе ссылку на предыдущий узел.
#  Обязательно вызвать конструктор базового класса тем самым дополняя функциональность
#  базового класса, сохраняя его логику.
#  Атрибут экземпляра prev сделать свойством prev.
#  Определить для него getter и setter с проверками аналогичными свойству next в классе Node.
#  Для DoubleLinkedNode подумать какой из методов
#  __repr__, метод __str__ наследовать, а какой перегрузить.