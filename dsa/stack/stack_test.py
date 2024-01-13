import unittest
from dsa.stack.dynamic_array_stack import DynamicArrayStack
from dsa.stack.linked_list_stack import LinkedListStack


class TestDynamicArrayStack(unittest.TestCase):
    def test_dynamic_array_stack_init(self):
        r"""Should create a dynamic array stack containing three elements."""
        stack = DynamicArrayStack()
        stack.push(3)
        stack.push(2)
        stack.push(1)

        self.assertEqual(stack.size, 3)

        self.shortDescription()

    def test_dynamic_array_stack_push_and_pop(self):
        r"""Should push and pop elements of a stack following LIFO principle."""
        stack = DynamicArrayStack()
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

    def test_dynamic_array_stack_peek(self):
        r"""Should peek the top element of a dynamic array stack."""
        stack = DynamicArrayStack()
        stack.push(3)
        stack.push(2)
        stack.push(1)

        value = stack.peek()
        self.assertEqual(value, 1)
        self.assertEqual(stack.size, 3)

        self.shortDescription()


class TestLinkedListStack(unittest.TestCase):
    def test_linked_list_stack_init(self):
        r"""Should create a linked list stack containing three elements."""
        stack = LinkedListStack()
        stack.push(3)
        stack.push(2)
        stack.push(1)

        self.assertEqual(stack.size, 3)
        self.shortDescription()

    def test_linked_list_stack_push_and_pop(self):
        r"""Should push and pop elements of a stack following LIFO principle."""
        stack = LinkedListStack()
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

    def test_linked_list_stack_peek(self):
        r"""Should peek the top element of a linked list stack."""
        stack = LinkedListStack()
        stack.push(3)
        stack.push(2)
        stack.push(1)

        value = stack.peek()
        self.assertEqual(value, 1)
        self.assertEqual(stack.size, 3)

        self.shortDescription()