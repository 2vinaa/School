from queue import Queue

class PrintQueue:
    def __init__(self):
        self.job_queue = Queue()

    def add_job(self, document_name):
        self.job_queue.enqueue(document_name)

    def process_job(self):
        return self.job_queue.dequeue()

    def next_job(self):
        return self.job_queue.peek()

if __name__ == '__main__':
    printer = PrintQueue()
    printer.add_job("report.pdf")
    printer.add_job("thesis.docx")
    print(printer.process_job())  # returns "report.pdf"print(printer.next_job()) # prints "thesis.docx"
    print(printer.next_job())
    print(printer.process_job())
    print(printer.process_job())