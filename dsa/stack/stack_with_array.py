class StackWithArray:
    def __init__(self):
        self.stack = []

    @property
    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():  # Prevents `pop` to raise `IndexError`
            return None

        return self.stack.pop()  # Raises `IndexError` if list is empty

    def top(self):
        if self.is_empty():
            return None

        return self.stack[-1]  # Returns the value of the last element

    def peek(self):
        return self.top()

    def summary(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for element in self.stack[::-1]:
                print(element, end=" -> ")
            print("None")
