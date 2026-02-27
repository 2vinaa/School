from arr import Array

class Queue:
    def __init__(self, max_size):

        self.count = 0
        self.front = 0
        self.back = max_size-1
        self.theArray = Array(max_size)

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.theArray)

    def enqueue(self, value):
        assert not self.is_full() #cannot add to a full queue
        max_Size = len(self.theArray)
        self.back = (self.back + 1) % max_Size
        self.theArray[self.back] = value
        self.count += 1

    def dequeue(self):
        assert not self.is_empty() #cant remove from an empty queue
        max_Size = len(self.theArray)
        item = self.theArray.pop(self.front)
        self.front = (self.front+ 1) % max_Size
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