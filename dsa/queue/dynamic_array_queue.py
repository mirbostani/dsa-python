class DynamicArrayQueue:
    def __init__(self):
        self.queue = []

    @property
    def size(self):
        return len(self.queue)

    def is_empty(self):
        r"""Checks if the queue is empty."""
        return len(self.queue) == 0

    def enqueue(self, data):
        r"""Adds an element to the rear of the queue."""
        self.queue.append(data)

    def dequeue(self):
        r"""Removes an element from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")

        return self.queue.pop(0)

    def peek(self):
        r"""Gets the value of the front element without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")

        return self.queue[0]
