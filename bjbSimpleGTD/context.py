# bjbSimpleGTD
#
# context.py
#

import uuid

class Context:

    def __init__(self, a_string):
        self.description = a_string
        self.uuid = uuid.uuid4()

    def get_description(self):
        return self.description

    def set_description(self, a_string):
        self.description = a_string

    def get_uuid(self):
        return self.uuid

