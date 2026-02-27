
class QNode:

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:

    def __init__(self):#, max_size):
        #self.__max_size = max_size
        self.__q_head = None
        self.__q_tail = None
        self.__current_size = 0 # counter

    def enqueue(self, item):
        #assert self.__current_size < self.__max_size, "Queue is full"
        node = QNode(item)
        if self.is_empty():
            self.__q_head = node
            self.__q_tail = self.__q_head
        else:
            self.__q_tail.next = node
            self.__q_tail = self.__q_tail.next
        self.__current_size += 1

    def dequeue(self):
        assert not self.is_empty(), "Queue is empty, cannot dequeue"
        item = self.__q_head.item
        self.__q_head = self.__q_head.next
        self.__current_size -= 1
        return item

    def peek(self):
        assert not self.is_empty(), "Queue is empty, cannot peek"
        return self.__q_head.item

    def __len__(self):
        return self.__current_size

    def is_empty(self):
        return self.__current_size == 0
        # return self.__q_head == self.__q_tail == None