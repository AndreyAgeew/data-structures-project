from typing import Any, Optional

from src.stack import Node


class LinkedListNode(Node):
    """Класс для узла односвязного списка"""


class LinkedList(LinkedListNode):
    """Класс для односвязного списка"""

    def __init__(self):
        """Конструктор класса LinkedList"""
        super().__init__(None)

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        return " -> ".join([str(elem) for elem in self]) + " -> None"

    def __iter__(self):
        """
        Возвращает итератор для односвязного списка

        :return: итератор для односвязного списка
        """
        current = self
        while current is not None:
            if current.data is not None:
                yield current.data
            current = current.next_node

    def insert_beginning(self, data: dict) -> None:
        """
        Метод для добавления узла с данными в начало списка

        :param data: данные, которые будут добавлены в узел
        """
        new_node = Node(data)
        new_node.next_node = self.next_node
        self.next_node = new_node

    def insert_at_end(self, data: dict) -> None:
        """
        Метод для добавления узла с данными в конец списка

        :param data: данные, которые будут добавлены в узел
        """
        new_node = Node(data)
        if self.next_node is None:
            self.next_node = new_node
        else:
            current = self.next_node
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node

    def to_list(self) -> list:
        """
        Метод для преобразования данных односвязного списка в список

        :return: список данных
        """
        data_list = []
        current = self.next_node
        while current is not None:
            data_list.append(current.data)
            current = current.next_node
        return data_list

    def get_data_by_id(self, value: Any) -> Optional[dict]:
        """
        Метод для получения первого словаря с указанным значением ключа 'id' из списка

        :param value: значение 'id' для поиска
        :return: словарь с указанным значением 'id' или None, если такого словаря не найдено
        """
        current = self.next_node
        while current is not None:
            try:
                if current.data['id'] == value:
                    return current.data
            except (TypeError, KeyError):
                print("Данные не являются словарем или в словаре нет id.")
            current = current.next_node
        return None
