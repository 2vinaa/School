# Node class for singly linked list
from operator import index


class ListNode:

    def __init__(self, data):
        self.data = data      # Value of the node
        self.next = None      # Pointer to the next node


    def __str__(self):
        return str(self.data)

# Linked list class
class LinkedList:

    def __init__(self):
        self.head = None      # First node in the list
        self.tail = None      # Last node in the list (for constant-time append)
        self.length = 0       # Number of nodes in the list

    # Append node with linear time complexity O(n)
    def append_linear(self, node):
        if self.head is None:
            # List is empty, set head to new node
            self.head = node
        else:
            # Traverse the list to find the last node
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.tail = node       # Update the tail reference
        self.length += 1       # Increment the length



    # Append node with constant time complexity O(1)
    def append_constant(self, node):
        if self.head is None:
            # List is empty, set head to new node
            self.head = node
        else:
            # Link new node after current tail
            self.tail.next = node
        self.tail = node       # Update the tail reference
        self.length += 1       # Increment the length


    def search_linear(self, target):
        current = self.head
        while current is not None:
            if current == target:
                return current
            else:
                current = current.next

        return None

    def get_ele_by_index(self, index):
        if index <0 or index >self.length:
            raise IndexError("Index out of range")
        current = self.head
        cindex = 0
        while cindex != index:
            current = current.next
            cindex += 1
        return current

    def add_after(self, target_node, new_node):
        previous_node = self.search_linear(target_node)
        if previous_node is None:
            raise IndexError("ListNode does not exist")

        if previous_node is not None:
            next_node = previous_node
            previous_node.next = new_node
            new_node.next = next_node
            self.length += 1

    def add_before(self, target_node, new_node):
        if target_node == self.head:
            new_node.next = self.head
            self.head = new_node

        previous_node = self.head
        curr_node = previous_node.next

        while curr_node.data != target_node and curr_node is not None:
            previous_node = curr_node
            curr_node = curr_node.next

        previous_node.next = new_node
        new_node.next = curr_node

    def remove(self, data_rem):
        if self.head is None:
            raise IndexError("List is Empty")

        previous = self.head
        current = previous.next

        while previous.data  != data_rem:
            previous = current
            current = current.next

        previous.next = current.next


    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "->".join(nodes) if nodes else "Empty List"




    # Print all elements in the list
    def print_list(self):
        current = self.head.next
        result = str(self.head.data)
        while current:
            result += ", " + str(current.data)
            current = current.next
        print(result)


# Example usage
if __name__ == '__main__':
    ll = LinkedList()
    ll.append_linear(ListNode(10))      # Appends 10 using linear append
    ll.append_constant(ListNode(20))    # Appends 20 using constant-time append
    ll.append_constant(ListNode(30))    # Appends 30 using constant-time append

    ll.print_list()                     # Should print 10, 20, 30
    print(ll.length)                    # Should print 3

    a = LinkedList()
    a.append_linear(ListNode(9))
    a.append_linear(ListNode(13))
    a.append_linear(ListNode(6))

    print(a.get_ele_by_index(2))


    print(ll.add_after(1, 2))