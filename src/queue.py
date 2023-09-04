class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        fullqueue = ''
        current = self.head
        while current:
            fullqueue += str(current.data) + '\n'  # переводим в str на случай, если кто-то добавит циферьки
            current = current.next_node
        return fullqueue.strip()  # удаляем последний перенос строки

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь
        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
        :return: данные удаленного элемента
        """
        if self.head is None:
            return

        data = self.head.data
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None

        return data
