class Node:
    """A node in the singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    """Stack implemented using a singly linked list."""
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self.top.value
        self.top = self.top.next
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.value