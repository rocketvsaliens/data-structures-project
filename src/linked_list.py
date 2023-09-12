class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self) -> None:
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self) -> list:
        """Возвращает список с данными из односвязного списка"""
        node = self.head
        data_list = []

        while node:
            data_list.append(node.data)
            node = node.next_node

        return data_list

    def get_data_by_id(self, target_id) -> dict or None:
        """Возвращает первый найденный словарь с ключом 'id', равным переданному значению"""
        node = self.head
        while node:
            try:
                if node.data['id'] == target_id:
                    return node.data

            except TypeError:
                # я бы сделала реализацию исключения чуть по-другому, но из мейна код не выкинешь ;)
                print('Данные не являются словарем или в словаре нет id.')

            node = node.next_node
