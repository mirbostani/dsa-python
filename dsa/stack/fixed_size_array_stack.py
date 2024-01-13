class FixedSizeArrayStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * self.max_size
        self.head = -1

    @property
    def size(self):
        return self.head + 1

    def is_empty(self):
        return self.head == -1    
    
    def is_full(self):
        return self.head == self.max_size - 1
    
    def push(self, data):
        if self.is_full():
            raise IndexError("Push to a full stack")
        
        self.head += 1
        self.stack[self.head] = data

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        
        popped_element = self.stack[self.head]
        self.stack[self.head] = None
        self.head -= 1
        return popped_element
    
    def top(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        
        return self.stack[self.head]
    
    def peek(self):
        return self.top()