import unittest
from dsa.queue.dynamic_array_queue import DynamicArrayQueue
from dsa.queue.two_stack_queue import TwoStackQueue

class TestSimpleQueue(unittest.TestCase):
    def test_simple_queue_init(self):
        r"""Should create a simple queue with three elements."""
        queue = DynamicArrayQueue()
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        self.assertEqual(queue.size, 3)
        self.shortDescription()

    def test_simple_queue_enqueue_dequeue(self):
        r"""Should enqueue and dequeue following FIFO principle."""
        queue = DynamicArrayQueue()
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        value = queue.dequeue()
        self.assertEqual(value, 3)

        value = queue.dequeue()
        self.assertEqual(value, 2)

        value = queue.dequeue()
        self.assertEqual(value, 1)

        self.assertTrue(queue.is_empty())

        self.shortDescription()

    def test_simple_queue_peek(self):
        r"""Should peek the front element."""
        queue = DynamicArrayQueue()
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        value = queue.peek()
        self.assertEqual(value, 3)

        self.assertEqual(queue.size, 3)

        self.shortDescription()


class TestTwoStackQueue(unittest.TestCase):
    def test_two_stack_queue_init(self):
        r"""Should create a two-stack queue with three elements."""
        queue = TwoStackQueue()
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        self.assertEqual(queue.size, 3)
        self.shortDescription()

    def test_two_stack_queue_enqueue_dequeue(self):
        r"""Should enqueue and dequeue following FIFO principle."""
        queue = TwoStackQueue()
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        value = queue.dequeue()
        self.assertEqual(value, 3)
        self.assertEqual(queue.size, 2)

        value = queue.dequeue()
        self.assertEqual(value, 2)
        self.assertEqual(queue.size, 1)

        value = queue.dequeue()
        self.assertEqual(value, 1)
        self.assertTrue(queue.is_empty())

    def test_two_stack_queue_peek(self):
        r"""Should peek the front element."""
        queue = TwoStackQueue()
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        value = queue.peek()
        self.assertEqual(value, 3)

        self.assertEqual(queue.size, 3)

        self.shortDescription()

