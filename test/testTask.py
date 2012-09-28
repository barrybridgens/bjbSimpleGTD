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
        self.task2 = task.Task('Another Task')
        self.assertNotEqual(self.task.get_uuid(), self.task2.get_uuid())

    def test_complete(self):
        self.assertFalse(self.task.is_complete())
        self.task.complete()
        self.assertTrue(self.task.is_complete())
        self.task.uncomplete()
        self.assertFalse(self.task.is_complete())

    def test_contexts(self):
        self.assertFalse(self.task.has_context())
        self.assertFalse(self.task.is_valid_in_context('@home'))
        self.task.add_context('@home')
        self.assertTrue(self.task.has_context())
        self.task.remove_context('INVALID CONTEXT')
        self.assertTrue(self.task.has_context())
        self.assertTrue(self.task.is_valid_in_context('@home'))
        self.task.remove_context('@home')
        self.assertFalse(self.task.is_valid_in_context('@home'))
        self.assertFalse(self.task.has_context())

if __name__ == '__main__':
    unittest.main()
