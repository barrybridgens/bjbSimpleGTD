# bjbSimpleGTD
#
# task.py
#

import uuid

class Task:

    def __init__(self, a_string):
        self.description = a_string
        self.uuid = uuid.uuid4()
        self.task_complete = False
        self.contexts = []

    def get_description(self):
        return self.description

    def set_description(self, a_string):
        self.description = a_string

    def get_uuid(self):
        return self.uuid

    def is_complete(self):
        return self.task_complete

    def complete(self):
        self.task_complete = True

    def uncomplete(self):
        self.task_complete = False

    def has_context(self):
        return (len(self.contexts) > 0)

    def is_valid_in_context(self, a_context):
        return(a_context in self.contexts)

    def add_context(self, a_context):
        self.contexts.append(a_context)

    def remove_context(self, a_context):
        if a_context in self.contexts:
            self.contexts.remove(a_context)

