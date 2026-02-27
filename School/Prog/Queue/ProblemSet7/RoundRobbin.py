class Process:
    def __init__(self, process_id, execution_time):
        self.process_id = process_id
        self.execution_time = execution_time

        self.__remaining_time = execution_time


    def execute(self, time_slice:int):
        self.__remaining_time -= time_slice

    def get_remaining_time(self):
        return self.__remaining_time