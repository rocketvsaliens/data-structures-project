import pytest
from src import queue

ATTR_ERROR_MSG = "'NoneType' object has no attribute 'data'"


def test_node_init():
    data = 5
    node = queue.Node(data)

    assert node.data == data
    assert node.next_node is None


def test_node_init_with_next_node():
    data = 'a'
    next_node = queue.Node(5)
    node = queue.Node(data, next_node)

    assert node.data == data
    assert node.next_node == next_node


@pytest.fixture
def test_queue():
    test_queue = queue.Queue()
    test_queue.enqueue('data1')
    test_queue.enqueue('data2')
    test_queue.enqueue('data3')
    return test_queue


def test__str__(test_queue):
    assert str(test_queue) == "data1\ndata2\ndata3"


def test_enqueue(test_queue):
    assert test_queue.head.data == 'data1'
    assert test_queue.head.next_node.data == 'data2'
    assert test_queue.tail.data == 'data3'
    assert test_queue.tail.next_node is None
    with pytest.raises(AttributeError):
        assert test_queue.tail.next_node.data == ATTR_ERROR_MSG
