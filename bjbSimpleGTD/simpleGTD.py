# bjbSimpleGTD
#
# simpleGTD.py
#

from task import Task
from context import Context

class simpleGTD:

    def __init__(self):
        self.tasks = {}
        self.contexts = {}

    # Tasks
    
    def add_task(self, a_string):
        t = Task(a_string)
        self.tasks[t.get_uuid()] = t

    # Contexts

    def add_context(self, a_string):
        c = Context(a_string)
        self.contexts[c.get_uuid()] = c

    # Debugging methods

    def dump_tasks(self):
        print('Task Dump:')
        for k, v in self.tasks.iteritems():
            print(k, v.get_description())

    def dump_contexts(self):
        print('Context Dump:')
        for k, v in self.contexts.iteritems():
            print(k, v.get_description())
