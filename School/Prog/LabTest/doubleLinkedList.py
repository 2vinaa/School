class DListNode:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def isEmpty(self):
        return self.head is None

    def append(self, new):
        new_node = DListNode(new)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            curnode = self.head
            while curnode and curnode.data < new_node.data:
                    curnode = curnode.next

            if curnode == self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

            elif curnode is None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

            else:
                prev_node = curnode.prev
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = curnode
                curnode.prev = new_node
        self.len += 1

    def remove(self,target):
        if self.isEmpty():
            return
        curnode = self.head
        while curnode:
            if curnode.data == target:
                if curnode == self.head:
                    self.head = curnode.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif curnode == self.tail:
                    self.tail = curnode.prev
                    if self.tail:
                        self.tail.next = None
                    else:
                        self.head = None
                else:
                    curnode.prev.next = curnode.next
                    curnode.next.prev = curnode.prev

                self.len -= 1
                return
            curnode = curnode.next

    def frontTraversal(self):
        curnode = self.head
        while curnode.next:
            print(curnode.data, end=" --- ")
            curnode = curnode.next
        print(curnode.data)

    def reversedTraversal(self):
        curnode = self.tail
        while curnode.prev:
            print(curnode.data, end=" --- ")
            curnode = curnode.prev
        print(curnode.data)

if __name__ == "__main__":
    ex = DLinkedList()
    ex.append(1)
    ex.append(4)
    ex.append(2)
    ex.append(7)
    ex.append(5)
    ex.append(1)
    ex.frontTraversal()
    ex.remove(1)
    ex.frontTraversal()
    ex.reversedTraversal()