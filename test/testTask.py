# Test task

import unittest

from bjbSimpleGTD import task

class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = task.Task('TestTask')

    def tearDown(self):
        self.task = None

    def test_description(self):
        self.assertEqual('TestTask', self.task.get_description())

    def test_uuid(self):
        self.assertEqual(4, self.task.get_uuid().version)

    def test_complete(self):
        self.assertFalse(self.task.is_complete())
        self.task.complete()
        self.assertTrue(self.task.is_complete())
        self.task.uncomplete()
        self.assertFalse(self.task.is_complete())

if __name__ == '__main__':
    unittest.main()