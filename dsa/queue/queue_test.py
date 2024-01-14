import unittest
from dsa.queue.queue_with_dynamic_array import QueueWithDynamicArray
from dsa.queue.queue_with_two_stacks import QueueWithTwoStacks
from dsa.queue.queue_with_fixed_size_array import QueueWithFixedSizeArray

class TestQueueWithDynamicArray(unittest.TestCase):
    def test_queue_with_dynamic_array_init(self):
        r"""Should create a simple queue with three elements."""
        queue = QueueWithDynamicArray()
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        self.assertEqual(queue.size, 3)
        self.shortDescription()

    def test_queue_with_dynamic_array_enqueue_dequeue(self):
        r"""Should enqueue and dequeue following FIFO principle."""
        queue = QueueWithDynamicArray()
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

    def test_queue_with_dynamic_array_peek(self):
        r"""Should peek the front element."""
        queue = QueueWithDynamicArray()
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        value = queue.peek()
        self.assertEqual(value, 3)

        self.assertEqual(queue.size, 3)

        self.shortDescription()


class TestQueueWithTwoStacks(unittest.TestCase):
    def test_queue_with_two_stacks_init(self):
        r"""Should create a two-stack queue with three elements."""
        queue = QueueWithTwoStacks()
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        self.assertEqual(queue.size, 3)
        self.shortDescription()

    def test_queue_with_two_stacks_enqueue_dequeue(self):
        r"""Should enqueue and dequeue following FIFO principle."""
        queue = QueueWithTwoStacks()
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

    def test_queue_with_two_stacks_peek(self):
        r"""Should peek the front element."""
        queue = QueueWithTwoStacks()
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        value = queue.peek()
        self.assertEqual(value, 3)

        self.assertEqual(queue.size, 3)

        self.shortDescription()

class TestQueueWithFixedSizeArray(unittest.TestCase):
    def test_queue_with_fixed_size_array_init(self):
        r"""Should create a queue with fixed-size array including three elements."""
        max_size = 3
        queue = QueueWithFixedSizeArray(max_size=max_size)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertTrue(queue.is_full())
        self.assertEqual(queue.front, 0)
        self.assertEqual(queue.rear, max_size - 1)
        self.shortDescription()

    def test_queue_with_fixed_size_array_enqueue_dequeue(self):
        r"""Should enqueue and dequeue following FIFO principle."""
        queue = QueueWithFixedSizeArray(max_size=3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        value = queue.dequeue()
        self.assertEqual(value, 1)

        value = queue.dequeue()
        self.assertEqual(value, 2)

        value = queue.dequeue()
        self.assertEqual(value, 3)

        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.front, -1)
        self.assertEqual(queue.rear, -1)
        self.shortDescription()

    def test_queue_with_fixed_size_array_peek(self):
        r"""Should peek the front element."""
        queue = QueueWithFixedSizeArray(max_size=3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        value = queue.peek()
        self.assertEqual(value, 1)
        self.shortDescription()

    def test_queue_with_fixed_size_array_dequeue_more_than_enqueue(self):
        r"""Should prevent dequeue if exceeds the number of enqueue."""
        queue = QueueWithFixedSizeArray(max_size=5)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        value = queue.dequeue()
        self.assertEqual(value, 1)

        value = queue.dequeue()
        self.assertEqual(value, 2)

        value = queue.dequeue()
        self.assertEqual(value, 3)

        with self.assertRaises(IndexError):
            value = queue.dequeue()

        self.shortDescription()