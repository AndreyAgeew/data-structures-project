from typing import Any, Optional

from typing import Any, Optional


class Node:
    """Класс для узла очереди"""

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


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        return f"Queue: {' -> '.join([str(item) for item in self])}"

    def __iter__(self):
        """
        Возвращает итератор для очереди

        :return: итератор для очереди
        """
        current = self.head
        while current is not None:
            yield current.data
            current = current.next_node

    def enqueue(self, data: Any) -> None:
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self) -> Any:
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
        Если очередь пуста, возвращает None.

        :return: данные удаленного элемента или None, если очередь пуста
        """
        if self.tail is None:
            return None

        data = self.head.data
        self.head = self.head.next_node

        if self.head is None:
            self.tail = None

        return data
