from RoundRobbin import Process
from QueueLinkedList import Queue

class Scheduler:
    def __init__(self, time_slice):
        self.time_slice = time_slice
        self.process_queue = Queue()

    def add_process(self, process: Process):
        self.process_queue.enqueue(process)

    def execute_process(self):
        while not self.process_queue.is_empty():
            current_process = self.process_queue.dequeue()
            print("Executing Process", current_process)
            current_process.execute(self.time_slice)

            if current_process.get_remaining_time() > 0:
                print("Rescheduling Process", current_process)
                self.add_process(current_process)



if __name__ == "__main__":

    sched = Scheduler(10)

    sched.add_process(Process(1, 500))
    sched.add_process(Process(2, 300))
    sched.add_process(Process(3, 700))
    sched.add_process(Process(4, 900))

    sched.execute_process()

