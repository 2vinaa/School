from LINKEDLISTADT import LinkedList


class Tasknode:
    def __init__(self, description):
        self.description = description
        self.next = None

    def __str__(self):
        return f"The Task has description : {self.description}"


class ToDoList:
    def __init__(self):
        self.head = None
        self.lista = []
        self.linkedlist = LinkedList()

    def add_task(self, task:Tasknode):
        if task not in self.lista:
            self.lista.append(task)
            if self.head is None:
                self.head = task
            return "The task has been successfully added"
        else:
            return "The task has not been added as it was already present"


    def remove_task(self, task:Tasknode):
        if task not in self.lista:
            return "Cannot remove something not present in ToDoList"
        else:
            self.lista.remove(task)
            if self.head is task:
                self.head = self.head.next
            return "Successfully removed the task"

    def add_linked_task(self, task:Tasknode):
        if self.linkedlist.search_linear(task) is None:
            self.linkedlist.append_constant(task)
            if self.head is None:
                self.head = task
            return "The task has been successfully added"
        else:
            return "The task has not been added as it was already present"


    def remove_linked_task(self, task:Tasknode):
        if self.linkedlist.search_linear(task) is not None:
            self.linkedlist.remove(task)
            if self.head is task:
                self.head = self.head.next
            return "The task has been removed"
        else:
            return "Cannot remove something not present in ToDoList"


    def __str__(self):
        result = self.linkedlist.head.data
        curr = self.linkedlist.head.next


        while curr:
            data = curr
            result += "\n\n" + str(data)
            curr = curr.next

        return result






