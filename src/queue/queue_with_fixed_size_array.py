class QueueWithFixedSizeArray:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * self.max_size
        self.rear = -1
        self.front = -1

    def is_empty(self) -> bool:
        r"""Checks if the queue is empty."""
        return self.front == -1

    def is_full(self) -> bool:
        r"""Checks if the queue is full."""
        return self.rear == self.max_size - 1

    def enqueue(self, data):
        r"""Adds an element to the rear of the queue."""
        if self.is_full():
            raise IndexError("Enqueue to a full queue")

        # First enqueue operation
        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = data

    def dequeue(self):
        r"""Removes and returns an element from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")

        dequeued_element = self.queue[self.front]
        self.queue[self.front] = None  # Does not work for referenced objects

        # Prevents dequeue if exceeds the number of enqueue
        if self.front >= self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        return dequeued_element
    
    def peek(self):
        r"""Gets the value of the front element without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        
        return self.queue[self.front]

    def summary(self):
        print(self.queue, f"front:{self.front}", f"rear:{self.rear}")
