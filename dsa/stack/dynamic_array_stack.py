class DynamicArrayStack:
    def __init__(self):
        self.stack = []

    @property
    def size(self):
        return len(self.stack)

    def is_empty(self):
        r"""
        Checks if the stack is empty.

        The time complexity is $O(1)$, as the method involves a constant-time
        operation to check whether the length of the stack is equal to 0,
        regardless of the size of the stack.

        The space complexity is $O(1)$, as the method does not use additional
        space that scales with the size of the input.
        """
        return len(self.stack) == 0

    def push(self, data):
        r"""
        Pushes an element to the top of the stack.

        The time complexity is $O(1)$. In general, the `append` operation for
        a Python list has an amortized constant time complexity. However,
        occasionally, when the underlying dynamic array needs to be resized,
        the operation may take $O(n)$ time due to copying elements to a larger
        array. While individual `push` operations might occasionally be more
        expensive due to resizing, the average cost per `push` operation is
        constant over a sequence of operations.

        The space complexity is $O(1)$, as the method appends a single element
        to the list, and the space required for this operation is constant.
        """
        self.stack.append(data)

    def pop(self):
        r"""
        Removes an element from the top of the stack.

        The time complexity is $O(1)$, as the `pop` operation for a Python list,
        in general, has a constant time complexity. It involves removing the
        last element from the list, which can be done in constant time.

        The space complexity is $O(1)$, as the method removes a single element
        from the list, and the space required for this operation is constant.
        """
        if self.is_empty():
            return IndexError("Pop from an empty stack")

        return self.stack.pop()  # Raises `IndexError` if list is empty

    def top(self):
        r"""
        Returns the top element without removing it from the stack.

        The time complexity is $O(1)$, as accessing the last element of a Python
        list using the `[-1]` index is a constant-time operation.

        The space complexity is $O(1)$, as the method does not use additional
        space that scales with the size of the input.
        """
        if self.is_empty():
            return IndexError("Peek from an empty stack")

        return self.stack[-1]  # Returns the value of the last element

    def peek(self):
        r"""
        An alias for `top`.
        """
        return self.top()

    def summary(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for element in self.stack[::-1]:
                print(element, end=" -> ")
            print("None")
