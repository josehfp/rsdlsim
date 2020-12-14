from Task import Task


class Cpu:
    def __init__(self, scheduler):
        self.cur_task = None
        self.clock = 0
        self.cur_id = 1
        self.scheduler = scheduler

    def print(self):
        print("CPU Time:%3d" % self.clock)
        print(self.scheduler)

    def next_clock(self):
        self.clock = self.clock + 1
        self.scheduler.schedule()

    def next_id(self):
        self.cur_id = self.cur_id + 1
        return self.cur_id

    def create_n_randon_tasks(self, quantity):
        for i in range(quantity):
            task = Task(self.next_id())
            self.scheduler.queue(task)

    def run(self):
        while True:
            self.print()
            print("[N]ext, [B]lock, [E]xit: ")
            option = input()
            if option == 'e' or option == 'E':
                return
            self.next_clock()
