from typing import Iterable, Any, Optional, Iterator
from collections.abc import MutableSequence
from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):

    def __init__(self, data: Iterable = None):
        """
        Конструктор связанного списка
        """
        self._len = 0
        self._head = Optional[Node] = None
        self._tail = self._head

        self.extend(data)

    def step_by_step_on_nodes(self, index: int) -> [Node, DoubleLinkedNode]:
        """
        Перемещение по узлам до указанного индекса
        и возвращает значение
        """
        self.validate_index(index)

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def validate_index(self, index: int):
        """
        Проверяет, индекс на правильность значения
        """
        if not isinstance(index, int):
            raise TypeError
        if not 0 <= index < self._len:
            raise IndexError

    def linked_nodes(self, left_node: Node, right_node: Optional["Node"] = None) -> None:
        """
        Связывает между собой два узла ноды в односвязном списке
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """
        Возвращает значение узла по указанному индексу
        """

        self.validate_index(index)
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """
        Устанавливает значение узла по указанному индексу
        """

        self.validate_index(index)
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int) -> None:
        """
        Удаляет элемент по указанному индексу
        """

        self.validate_index(index)

        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            self._tail = self.step_by_step_on_nodes(index - 1)
            self._tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            current_node_del = prev_node.next
            next_node = current_node_del.next
            self.linked_nodes(prev_node, next_node)

        self._len -= 1

    def __len__(self) -> int:
        """
        Возвращает длину связанного списка
        """
        return self._len

    def __str__(self) -> str:
        """
        Возвращает представление списка нод для пользователя
        """
        return f"{self.to_list()}"

    def __repr__(self) -> str:
        """
        Возвращает представление списка нод
        """
        return f"{self.__class__.__name__}({self.to_list()})"

    def insert(self, index: int, value: Any) -> None:
        """
        Добавляет значение по указанному индексу
        """
        if not isinstance(index, int):
            raise TypeError
        if not 0 <= index <= self._len:
            raise IndexError
        insert_node = Node(value)

        if index == 0:
            insert_node.next = self._head
            self._head = insert_node
            self._len += 1
        elif index >= self._len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

            self._len += 1

    def append(self, value: Any) -> None:
        """
        Добавляет значение в конец списка
        """
        append_node = Node(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def node_iterator(self) -> Iterator:
        """
        Проходит по всем узлам нод
        """
        current_node = self._head
        for _ in range(self._len):
            yield current_node
            current_node = current_node.next

    def __iter__(self) -> Iterator:
        """
        Итерируется по узлам нод и возвращает значение
        """
        for node in self.node_iterator():
            yield node.value

    def __contains__(self, item: Any) -> bool:
        """
        Проверяед вхождение элемента в список
        """
        for node in self.node_iterator():
            if node.value == item:
                return True
        return False

    def reversed_iter_(self) -> Iterator:
        """
        Проходит по всем узлам нод
        """
        for index in range(self._len - 1, -1, -1):
            current_node = self.step_by_step_on_nodes(index)
            yield current_node

    def __reversed__(self) -> Iterator:
        """
        Возвращает значение списка в обратном порядке
        """
        for node in self.reversed_iter_():
            yield node.value

    def count(self, item: Any) -> int:
        """
        Считает количество вхождений указанного значения в список
        """
        count = 0
        for value in self:
            if value == item:
                count += 1
        return count

    def to_list(self):
        pass


class DoubleLinkedList(LinkedList):
    def linked_nodes(self, left_node: DoubleLinkedNode, right_node: Optional["DoubleLinkedNode"] = None) -> None:
        """
        Связывает между собой два узла ноды в двунаправленом списке
        """
        left_node.next = right_node
        right_node.prev = left_node

    def create_node(self, value: Any) -> DoubleLinkedNode:
        return DoubleLinkedNode(value)

    def reversed_iter_nodes(self) -> Iterator:
        current_node = self._tail
        for _ in range(self._len):
            yield current_node
            current_node = current_node.prev

    def __delitem__(self, index: int) -> Any:
        """
        Удаляет элемент по указанному индексу
        """
        if not isinstance(index, int):
            raise TypeError()
        else:
            current_index = 1
            right_node = self._head
            left_node = None

            while right_node is not None:
                if current_index == index:
                    if left_node is not None:
                        left_node.next = right_node.next
                        right_node.next.prev = left_node
                    else:
                        self.head = right_node.next
                        return

                left_node = right_node
                right_node = right_node.next
                current_index += 1
            self._len = self._len - 1
            return


if __name__ == "__main__":
    ...

#  Двусвязный список на основе односвязного списка.
#  Односвязный список LinkedList должен быть унаследован
#  он абстрактного типа MutableSequence из модуля collections.abc.
#  В односвязном списке должны быть реализованы следующие методы:
    #  __getitem__
    #  __setitem__
    #  __delitem__
    #  __len__
    #  __str__
    #  __repr__
    #  insert
    #  append
#  Все атрибуты должны быть инкапсулированы.
#  То есть быть либо private или protected по вашему выбору.
#  Двусвязный список DoubleLinkedList должен наследоваться от LinkedList.
#  Для экземпляров данного класса должны работать все методы базового класса.
#  Необязательно все эти методы должны быть перегружены.
#  По максимуму используйте наследование, если поведение
#  списков в контексте реализации указанных метод схоже.
#  С точки зрения наследования по минимуму перегружайте методы.
#  При необходимости рефакторите базовый класс, чтобы локализовать части кода во вспомогательные функции,
#  которые имеют различное поведение в связном и двусвязном списках.
#  Стремитесь к минимизации кода в дочернем классе.

#  Дополнительные задания:
#  Эти задания приветствуются, но оцениваться не будут.
#  Будут вам плюсиком в карму.
#  Реализовать следующие методы:
    #  __iter__
    #  __contains__
    #  __reversed__
    #  count
    #  pop
    #  extend
    #  remove
    #  index