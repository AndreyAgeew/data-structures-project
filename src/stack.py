from typing import Any, Optional


class Node:
    """Класс для узла стека"""

    def __init__(self, data: Any, next_node: Optional['Node'] = None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :type data: Any
        :param next_node: ссылка на следующий узел в стеке (по умолчанию: None)
        :type next_node: Optional[Node]
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top: Optional[Node] = None

    def __iter__(self):
        """
        Возвращает итератор для стека

        :return: итератор для стека
        """
        current = self.top
        while current is not None:
            yield current.data
            current = current.next_node

    def __str__(self) -> str:
        """
        Возвращает строковое представление стека

        :return: строковое представление стека
        :rtype: str
        """
        return "Stack is empty" if self.top is None else "Stack: " + " -> ".join([str(item) for item in self])

    def push(self, data: Any) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        :type data: Any
        """
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next_node = self.top
            self.top = new_node

    def pop(self) -> Any:
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        :rtype: Any
        :raises Exception: если стек пустой
        """
        if self.top is None:
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next_node
        return data
