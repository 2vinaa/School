class CListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def isEmpty(self):
        return self.head is None

    def append(self, new):
        new_node = CListNode(new)

        if self.isEmpty():
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node

        else:
            current = self.head

            if new < self.head.data:
                tail = self.head.prev
                new_node.next = self.head
                new_node.prev = tail
                tail.next = new_node
                self.head.prev = new_node
                self.head = new_node

            else:
                while current.next != self.head and current.next.data < new:
                    current = current.next
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node

        self.len += 1


    def frontTraversal(self):
        curnode = self.head
        if curnode == self.head:
            print(curnode.data, end= " --- ")
            curnode = curnode.next
        while True:
            print(curnode.data, end=" --- ") if curnode.next != self.head else print(curnode.data)
            curnode = curnode.next
            if curnode == self.head:
                break


    def reversedTraversal(self):
        tail = self.head.prev
        curnode = tail
        if curnode == tail:
            print(curnode.data, end= " --- ")
            curnode = curnode.prev
        while True:
            print(curnode.data, end=" --- ") if curnode.prev != tail else print(curnode.data)
            curnode = curnode.prev
            if curnode == tail:
                break