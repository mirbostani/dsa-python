import unittest
from dsa.stack.stack_with_dynamic_array import StackWithDynamicArray
from dsa.stack.stack_with_linked_list import StackWithLinkedList
from dsa.stack.stack_with_fixed_size_array import StackWithFixedSizeArray


class TestStackWithDynamicArray(unittest.TestCase):
    def test_stack_with_dynamic_array_init(self):
        r"""Should create a stack with dynamic array containing three elements."""
        stack = StackWithDynamicArray()
        stack.push(3)
        stack.push(2)
        stack.push(1)

        self.assertEqual(stack.size, 3)

        self.shortDescription()

    def test_stack_with_dynamic_array_push_and_pop(self):
        r"""Should push and pop elements of a stack following LIFO principle."""
        stack = StackWithDynamicArray()
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

    def test_stack_with_dynamic_array_peek(self):
        r"""Should peek the top element of a dynamic array stack."""
        stack = StackWithDynamicArray()
        stack.push(3)
        stack.push(2)
        stack.push(1)

        value = stack.peek()
        self.assertEqual(value, 1)
        self.assertEqual(stack.size, 3)

        self.shortDescription()


class TestStackWithLinkedList(unittest.TestCase):
    def test_stack_with_linked_list_init(self):
        r"""Should create a stack with linked list containing three elements."""
        stack = StackWithLinkedList()
        stack.push(3)
        stack.push(2)
        stack.push(1)

        self.assertEqual(stack.size, 3)
        self.shortDescription()

    def test_stack_with_linked_list_push_and_pop(self):
        r"""Should push and pop elements of a stack following LIFO principle."""
        stack = StackWithLinkedList()
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

    def test_stack_with_linked_list_peek(self):
        r"""Should peek the top element of a linked list stack."""
        stack = StackWithLinkedList()
        stack.push(3)
        stack.push(2)
        stack.push(1)

        value = stack.peek()
        self.assertEqual(value, 1)
        self.assertEqual(stack.size, 3)

        self.shortDescription()


class TestStackWithFixedSizeArray(unittest.TestCase):
    def test_stack_with_fixed_size_array_init(self):
        r"""Should create a stack with fixed-size array containing three elements."""
        stack = StackWithFixedSizeArray(10)
        stack.push(3)
        stack.push(2)
        stack.push(1)

        self.assertEqual(stack.size, 3)
        self.assertEqual(stack.max_size, 10)

        self.shortDescription()

    def test_stack_with_fixed_size_array_push_and_pop(self):
        r"""Should push and pop elements of a stack following LIFO principle."""
        stack = StackWithFixedSizeArray(10)
        stack.push(3)
        stack.push(2)
        stack.push(1)

        value = stack.pop()
        self.assertEqual(value, 1)

        value = stack.pop()
        self.assertEqual(value, 2)

        value = stack.pop()
        self.assertEqual(value, 3)

        self.shortDescription()

    def test_stack_with_fixed_size_array_full(self):
        r"""Should prevent adding more elements when stack is full."""
        stack = StackWithFixedSizeArray(max_size=3)
        stack.push(3)
        stack.push(2)
        stack.push(1)

        self.assertTrue(stack.is_full())

        with self.assertRaises(IndexError):
            stack.push(0)

        self.shortDescription()

    def test_stack_with_fixed_size_array_empty(self):
        r"""Should prevent popping from an empty stack."""
        stack = StackWithFixedSizeArray(max_size=3)

        self.assertTrue(stack.is_empty())

        with self.assertRaises(IndexError):
            value = stack.pop()

        self.shortDescription()
