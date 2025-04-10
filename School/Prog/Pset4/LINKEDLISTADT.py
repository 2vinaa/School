# Node class for singly linked list
class ListNode:
    def __init__(self, data):
        self.data = data      # The actual value stored in the node
        self.next = None      # Pointer to the next node in the list (None by default)

    def __str__(self):
        return str(self.data) # String representation for easy printing


# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None      # Reference to the first node in the list
        self.tail = None      # Reference to the last node for fast O(1) appends
        self.length = 0       # Counter to keep track of the number of nodes

    # Append node with linear time complexity O(n)
    def append_linear(self, node):
        if self.head is None:
            # List is empty, set both head and tail to the new node
            self.head = node
            self.tail = node
        else:
            # Traverse the list until the end
            current = self.head
            while current.next is not None:
                current = current.next
            # Link the last node to the new node
            current.next = node
            self.tail = node  # Update the tail reference
        self.length += 1      # Increase list size by one

    # Append node with constant time complexity O(1) using the tail pointer
    def append_constant(self, node):
        if self.head is None:
            # List is empty, set both head and tail
            self.head = node
            self.tail = node
        else:
            # Connect the new node to the current tail and update tail
            self.tail.next = node
            self.tail = node
        self.length += 1      # Update size

    # Linear search to find a node with the same data as the target
    def search_linear(self, target):
        current = self.head
        while current is not None:
            if current.data == target.data:
                return current  # Found a node with matching data
            current = current.next
        return None             # Not found

    # Insert new_node after target_node (O(n) due to search)
    def add_after(self, target_node: ListNode, new_node: ListNode):
        previous_node = self.search_linear(target_node)
        if previous_node is None:
            raise IndexError("Target node not found")

        # Re-link the pointers to insert the new node
        new_node.next = previous_node.next
        previous_node.next = new_node

        # Update tail if we added at the end
        if previous_node == self.tail:
            self.tail = new_node

        self.length += 1

    # Insert new_node before target_node (O(n))
    def add_before(self, target_node: ListNode, new_node: ListNode):
        if self.head is None:
            raise IndexError("List is empty")

        if self.head.data == target_node.data:
            # Inserting before the head
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return

        previous_node = self.head
        current_node = self.head.next

        # Traverse until the target node is found
        while current_node is not None and current_node.data != target_node.data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            raise IndexError("Target node not found")

        # Insert new_node between previous and current
        previous_node.next = new_node
        new_node.next = current_node
        self.length += 1

    # Remove first node that matches the given data
    def remove(self, data):
        if self.length == 0:
            raise IndexError("List is empty")

        if self.head.data == data:
            # Remove the head
            self.head = self.head.next
            if self.head is None:
                self.tail = None  # List is now empty
            self.length -= 1
            return

        previous = self.head
        current = self.head.next

        # Traverse until the node to remove is found
        while current is not None and current.data != data:
            previous = current
            current = current.next

        if current is None:
            raise IndexError("Data not found")

        # Remove the node by skipping it
        previous.next = current.next

        if current == self.tail:
            self.tail = previous  # Update tail if we removed last node

        self.length -= 1

    # Return the data at a specific index (0-based)
    def get_element_by_index(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        current = self.head
        current_index = 0

        # Traverse to the correct index
        while current_index != index:
            current = current.next
            current_index += 1

        return current.data
    
    # overload the str conversion
    def __str__(self):
        if self.head is None:
            return "Empty"

        result = str(self.head.data)
        current = self.head.next

        # Traverse and append each element to the result string
        while current:
            result += ",\t" + str(current.data)
            current = current.next

        return result


    # Print all elements in the list in order
    def print_list(self):
        print(self.__str__())


# Example usage and test
if __name__ == '__main__':
    ll = LinkedList()
    ll.append_linear(ListNode(1))
    ll.append_linear(ListNode(2))
    ll.append_linear(ListNode(3))
    ll.append_linear(ListNode(5))
    ll.append_linear(ListNode(6))
    ll.append_constant(ListNode(7))

    ll.print_list()

    ll.add_after(ListNode(3), ListNode(4))  # Insert 4 after 3
    ll.print_list()

    ll.add_before(ListNode(3), ListNode(2.5))  # Insert 2.5 before 3
    ll.print_list()

    ll.remove(1)  # Remove head
    ll.print_list()

    ll.remove(7)  # Remove tail
    ll.print_list()

    ll.remove(10)  # Try to remove non-existent element (throws exception)