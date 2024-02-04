class StackWithFixedSizeArray:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * self.max_size
        self.head = -1

    @property
    def size(self):
        return self.head + 1

    def is_empty(self):
        return self.head == -1    
    
    def is_full(self):
        return self.head == self.max_size - 1
    
    def push(self, item):
        if self.is_full():
            raise IndexError("Push to a full stack")
        
        self.head += 1
        self.items[self.head] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        
        item = self.items[self.head]
        self.items[self.head] = None
        self.head -= 1
        return item
    
    def top(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        
        return self.items[self.head]
    
    def peek(self):
        return self.top()