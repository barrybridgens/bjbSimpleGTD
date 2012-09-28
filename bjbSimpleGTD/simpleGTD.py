# bjbSimpleGTD
#
# simpleGTD.py
#

from task import Task

class simpleGTD:

    def __init__(self):
        self.tasks = {}
    
    def add_task(self, a_string):
        t = Task(a_string)
        self.tasks[t.get_uuid()] = t

    # Debugging methods

    def dump_tasks(self):
        pass
