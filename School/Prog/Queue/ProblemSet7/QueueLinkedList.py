class QueueNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.count

    def enqueue(self, item):

        if self.is_empty():
            self.head = QueueNode(item)
            self.tail = QueueNode(item)
        else:
            self.tail.next = QueueNode(item)
            self.tail = self.tail.next
            self.count += 1

    def dequeue(self):
        if self.is_empty():
            return "Can't Remove from an Empty List"
        elif self.head == self.tail:
            item  = self.head
            self.head = None
            self.tail = None
            self.count = 0
            return item
        else:
            item = self.head
            self.head = self.head.next
            self.count -= 1
            return item


class BoundedPrioQueue:
    def __init__(self, numlevels):
        self.qSize = 0
        self.qLevels = Array(numlevels)
        for i in range(numlevels):
            self.qLevels[i] = Queue()

    def enqueue(self,item,priority):
        assert priority >= 0 and priority < len(self.qLevels), "invalid Prio levels"
        self.qLevels[priority].enqueue(item)
        self.qSize += 1

    def dequeue(self):
        assert not self.isEmpty(), "Cannot remove from an empty list"
        for i in range(len(self.qLevels)):
            if not self.qLevels[i].isEmpty():
                break
        self.qSize -= 1
        return self.qLevels[i].dequeue()
