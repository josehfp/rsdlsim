from Constants import MAX_PRIORITY


class Rsdl:
    def __init__(self):
        self.prio_rotation = 0
        self.cur_prio = 0
        self.static_bitmap = list()
        self.dyn_bitmap = list()
        self.active_list = list()
        self.inactive_list = list()
        self.quota = list()
        self.cur_task = None
        for i in range(MAX_PRIORITY + 1):
            self.static_bitmap.append(False)
            self.dyn_bitmap.append(False)
            self.active_list.append(list())
            self.inactive_list.append(list())
            # Todo parametrizar quantidade de cota por prioridade
            self.quota.append(0)

    def __repr__(self):
        string = "===Scheduler RSDL===\n"
        string += "Epoch:" + str(self.prio_rotation) + "\n"
        string += "Cur Prio:" + str(self.cur_prio) + "\n"
        string += "Sta Bitmap:" + str(self.static_bitmap) + "\n"
        string += "Dyn Bitmap:" + str(self.dyn_bitmap) + "\n"
        string += "Cur Task:" + repr(self.cur_task) + "\n"
        string += "===Active Queues===\n"
        i = 0
        for p in self.active_list:
            string += "P" + str(i) + "[" + str(self.quota[i]) + "]: " + str(p) + "\n"
            i = i + 1
        string += "===Inactive Queues===\n"
        i = 0
        for p in self.inactive_list:
            if len(p) > 0:
                string += "P" + str(i) + "[" + str(self.quota[i]) + "]: " + str(p) + "\n"
            i = i + 1
        string += "============\n"
        return string

    def recalc_task_prio(self, task):
        if task.rotation < self.prio_rotation:
            task.prio = task.static_prio
            task.replenish_quota()
            task.update_bitmap(task.static_prio)
            self.update_bitmap(task)
            self.quota[task.static_prio] += task.static_quota
            self.active_list[task.static_prio].append(task)
        else:
            if task.quota > 0 and self.quota[self.cur_prio] > 0:
                self.active_list[self.cur_prio].append(task)
            else:
                next_prio = task.get_next_prio()
                if next_prio >= 0:
                    self.quota[next_prio] = task.quota
                    self.active_list[next_prio].append(task)
                else:
                    task.clear_bitmap()
                    self.inactive_list[task.static_prio].append(task)

    def update_bitmap(self, task):
        self.static_bitmap[task.static_prio] = True
        self.dyn_bitmap[task.prio] = True

    def scheduler_tick(self):
        self.cur_task.quota -= 1
        if self.cur_task.quota <= 0:
            self.recalc_task_prio(self.cur_task)

    def task_run_tick(self):
        self.quota[self.cur_prio] -= 1
        if self.quota[self.cur_prio] <= 0:
            if self.cur_prio < 2:
                self.minor_epoch()
            else:
                self.major_epoch()
        else:
            self.scheduler_tick()

    def minor_epoch(self):
        # any tasks that have been merged will now have invalid values in p->prio so this must be considered
        self.active_list[self.cur_prio + 1].append(self.active_list[self.cur_prio][:])
        self.active_list[self.cur_prio] = list()
        self.cur_prio = self.cur_prio + 1

    def major_epoch(self):
        if self.cur_prio + 1 <= MAX_PRIORITY:
            # any tasks that have been merged will now have invalid values in p->prio so this must be considered
            self.inactive_list[self.cur_prio].append(self.active_list[self.cur_prio][:])
            self.active_list[self.cur_prio] = list()
            self.cur_prio = self.cur_prio + 1
            self.prio_rotation = self.prio_rotation + 1
        else:
            return
        pass

    def dequeue(self):
        if len(self.active_list[self.cur_prio]) == 0:
            self.dyn_bitmap[self.cur_prio] = False

    def schedule(self):
        first_list_index = self.find_first_list()
        if first_list_index > MAX_PRIORITY:
            self.major_epoch()
            return
        else:
            self.cur_prio = first_list_index
            self.cur_task = self.active_list[self.cur_prio].pop(0)



    def find_first_list(self):
        index = -1
        try:
            index = self.dyn_bitmap.index(True)
        except IndexError:
            index = -1
        return index

    def queue(self, task):
        self.recalc_task_prio(task)
