class QueueWithTwoStacks:
    r"""
    Two stacks are used to simulate a queue. Elements can be enqueued at one end
    and dequeued from the other.
    """
    
    def __init__(self):
        self.stack1 = []  # Enqueue stack
        self.stack2 = []  # Dequeue stack

    @property
    def size(self):
        return len(self.stack1) + len(self.stack2)

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def enqueue(self, data):
        r"""Adds an element to the back of the queue."""
        self.stack1.append(data)

    def dequeue(self):
        r"""Removes an element from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")

        # Move elements from stack1 (enqueue) to stack2 (dequeue) if stack2
        # is empty.
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        
        if not self.stack2: # if empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]
