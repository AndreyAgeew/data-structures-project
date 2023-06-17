from typing import Any, Optional

from src.stack import Node


class Queue(Node):
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        super().__init__(None)
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
