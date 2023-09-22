class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        ejected = self.top.data
        self.top = self.top.next_node
        return ejected

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.top is None:
            return ""
        else:
            return f"{self.top.data}\n{self.top.next_node.data}\n{self.top.next_node.next_node.data}"
