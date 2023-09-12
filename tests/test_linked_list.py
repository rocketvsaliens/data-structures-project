"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class NodeTestCase(unittest.TestCase):
    def test_node_creation(self):
        data = {'id': 1}
        node = Node(data)
        self.assertEqual(node.data, data)
        self.assertIsNone(node.next_node)


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_init(self):
        self.assertIsNone(self.ll.head)

    def test_insert_beginning(self):
        data = {'id': 1}
        self.ll.insert_beginning(data)
        self.assertEqual(self.ll.head.data, data)

    def test_insert_at_end(self):
        data = {'id': 0}
        data1 = {'id': 1}
        self.ll.insert_at_end(data1)
        self.assertEqual(self.ll.head.data, data1)
        self.ll.insert_beginning(data)
        self.assertEqual(self.ll.head.data, data)

    def test_str(self):
        self.assertEqual(str(self.ll), "None")
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(str(self.ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        expected_list = [{'id': 0, 'username': 'serebro'}, {'id': 1, 'username': 'lazzy508509'},
                         {'id': 2, 'username': 'mik.roz'}, {'id': 3, 'username': 'mosh_s'}]
        actual_list = self.ll.to_list()
        self.assertEqual(actual_list, expected_list)

    def test_get_data_by_id(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.assertEqual(self.ll.get_data_by_id(3), {'id': 3, 'username': 'mosh_s'})

    def test_get_data_by_id_exception(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end([1, 2, 3])
        user_data = self.ll.get_data_by_id(2)
        self.assertIsNone(user_data)


if __name__ == '__main__':
    unittest.main()
