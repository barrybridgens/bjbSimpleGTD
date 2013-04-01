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

    def task_exists(self, a_string):
        exists = False
        for k, v in self.tasks.iteritems():
            if a_string == v.get_description():
                exists = True
        return(exists)

    def task_by_uuid(self, a_uuid):
        return(self.tasks[a_uuid])

    def get_task_uuid(self, a_string):
        uuid = None
        for k, v in self.tasks.iteritems():
            if a_string == v.get_description():
                uuid = k
        return(uuid)


    # Contexts

    def add_context(self, a_string):
        c = Context(a_string)
        self.contexts[c.get_uuid()] = c

    def get_tasks_for_context(self, a_context):
        tasks = {}
        for k, v in self.tasks.iteritems():
            if v.is_valid_in_context(a_context):
                tasks[k] = v
        return(tasks)

    def context_exists(self, a_string):
        exists = False
        for k, v in self.contexts.iteritems():
            if a_string == v.get_description():
                exists = True
        return(exists)

    def context_by_uuid(self, a_uuid):
        return(self.contexts[a_uuid])

    def get_context_uuid(self, a_string):
        uuid = None
        for k, v in self.contexts.iteritems():
            if a_string == v.get_description():
                uuid = k
        return(uuid)


    # Debugging methods

    def dump_tasks(self):
        print('Task Dump:')
        for k, v in self.tasks.iteritems():
            print(k, v.get_description())
            if v.has_context():
                print "  has contexts"
                for context in v.get_contexts():
                    print ('    ' + self.context_by_uuid(context).get_description())

    def dump_contexts(self):
        print('Context Dump:')
        for k, v in self.contexts.iteritems():
            print(k, v.get_description())
