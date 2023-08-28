import pytest
from src import stack

ATTR_ERROR_MSG = "'NoneType' object has no attribute 'data'"


def test_node_init():
    data = 5
    node = stack.Node(data)

    assert node.data == data
    assert node.next_node is None


def test_node_init_with_next_node():
    data = 'a'
    next_node = stack.Node(5)
    node = stack.Node(data, next_node)

    assert node.data == data
    assert node.next_node == next_node


@pytest.fixture
def test_stack():
    test_stack = stack.Stack()
    test_stack.push('data1')
    test_stack.push('data2')
    test_stack.push('data3')
    return test_stack


def test_push(test_stack):
    assert test_stack.top.next_node.data == 'data2'
    assert test_stack.top.next_node.next_node.data == 'data1'
    assert test_stack.top.next_node.next_node.next_node is None
    with pytest.raises(AttributeError):
        assert test_stack.top.next_node.next_node.next_node.data == ATTR_ERROR_MSG


def test_pop(test_stack):
    assert test_stack.pop() == 'data3'
    assert test_stack.pop() == 'data2'
    assert test_stack.pop() == 'data1'
    assert test_stack.top is None
    with pytest.raises(AttributeError):
        assert test_stack.pop() == ATTR_ERROR_MSG


def test__str__(test_stack):
    assert str(test_stack) == "data3\ndata2\ndata1"
