from random import randrange

from Constants import MAX_TASK_DURATION, MAX_PRIORITY
from Printer import *


class Task:
    def __init__(self, pid, duration=0, static_priority=0):
        self.pid = pid
        self.static_quota = 5
        self.quota = 0
        self.rotation = -1
        self.bitmap = None
        self.clear_bitmap()
        self.active = True
        if duration == 0:
            self.duration = randrange(5, MAX_TASK_DURATION + 1)
        else:
            self.duration = duration
        self.prio = 0
        if static_priority == 0:
            self.static_prio = randrange(MAX_PRIORITY + 1)
        else:
            self.static_prio = static_priority

    def __repr__(self):
        string = "[%02d]p%1d -> %02d/%02d" % (self.pid, self.static_prio, self.quota, self.duration)
        if self.static_prio == 0:
            return bluebg_txt(string)
        elif self.static_prio == 1:
            return redbg_txt(string)
        return greenbg_txt(string)

    def __str__(self):
        return "|[%02d]p%1d -> %02d/%02d|" % (self.pid, self.static_prio, self.quota, self.duration)

    def replenish_quota(self):
        self.quota = self.static_quota

    def update_bitmap(self, prio):
        self.bitmap[prio] = True

    def get_next_prio(self):
        index = -1
        try:
            index = self.bitmap[self.static_prio:].index(False)
        except IndexError:
            index = -1
        return index

    def clear_bitmap(self):
        self.bitmap = list()
        for i in range(MAX_PRIORITY + 1):
            self.bitmap.append(False)
