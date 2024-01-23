class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackWithLinkedList:
    r"""
    A stack is a linear data structure that follows the principle of Last In,
    First Out (LIFO), that is, the last element pushed onto the stack is removed
    first. A stack can be implemented using a linked list.
    """

    def __init__(self):
        self.head = None

    @property
    def size(self):
        r"""
        Returns the number of elements in the stack.

        Time Complexity: $O(n)$, where $n$ is the number of elements
        Space Complexity: $O(1)$
        """
        current_node = self.head
        counter = 0
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter

    def is_empty(self):
        return self.head is None

    def push(self, data):
        r"""
        Adds an element to the top of the stack.

        Time Complexity: $O(1)$
        Space Complexity: $O(1)$
        """
        new_node = Node(data)
        new_node.next = self.head  # Points the new node's next to the head.
        self.head = new_node  # Sets the new node as the head.

    def pop(self):
        r"""
        Removes and returns the element from the top of the stack.

        Time Complexity: $O(1)$
        Space Complexity: $O(1)$
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")

        popped_node = self.head
        self.head = self.head.next  # Sets the head to the head's next node
        return popped_node.data

    def top(self):
        r"""
        Returns the element at the top of the stack without removing it.

        Time Complexity: $O(1)$
        Space Complexity: $O(1)$
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")

        return self.head.data

    def peek(self):
        r"""
        An alias for `top`.
        """
        return self.top()

    def summary(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next  # Returns None on the last node
        print("None")
