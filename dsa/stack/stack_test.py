import unittest
from stack_with_array import StackWithArray


class TestStackWithArray(unittest.TestCase):
    def test_stack_with_array_initialization(self):
        r"""
        Should create a stack containing three elements.
        """
        stack = StackWithArray()
        stack.push(3)
        stack.push(2)
        stack.push(1)

        self.assertEqual(stack.size, 3)

        self.shortDescription()

    def test_stack_with_array_push_and_pop(self):
        r"""
        Should push and pop elements following LIFO principle.
        """
        stack = StackWithArray()
        stack.push(3)
        stack.push(2)
        stack.push(1)

        value = stack.pop()
        self.assertEqual(value, 1)

        value = stack.pop()
        self.assertEqual(value, 2)

        value = stack.pop()
        self.assertEqual(value, 3)

        self.assertTrue(stack.is_empty())

        self.shortDescription()

    def test_stack_with_array_peek(self):
        r"""
        Should peek the top element.
        """
        stack = StackWithArray()
        stack.push(3)
        stack.push(2)
        stack.push(1)

        value = stack.peek()
        self.assertEqual(value, 1)
        self.assertEqual(stack.size, 3)

        self.shortDescription()
