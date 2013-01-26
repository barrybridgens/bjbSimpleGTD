# Test context

import unittest

from bjbSimpleGTD import context

class TestContext(unittest.TestCase):

    def setUp(self):
        self.context = context.Context('TestContext')

    def tearDown(self):
        self.task = None

    def test_description(self):
        self.assertEqual('TestContext', self.context.get_description())
        self.context.set_description('New description')
        self.assertEqual('New description', self.context.get_description())

    def test_uuid(self):
        self.assertEqual(4, self.context.get_uuid().version)
        self.context2 = context.Context('Another Context')
        self.assertNotEqual(self.context.get_uuid(), self.context2.get_uuid())

if __name__ == '__main__':
    unittest.main()
