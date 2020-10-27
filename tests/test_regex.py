import sys 
import os
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", "noted"))

import constants
import re
import unittest


class TestRegex(unittest.TestCase):

    def setUp(self):
        self.pattern = constants.master_pattern

    def test_new(self):
        self.assertEqual(re.search(self.pattern, r"new file").groups(), ("new", None, None, "file", None))
        self.assertEqual(re.search(self.pattern, r"new file dir").groups(), ("new", None, None, "file", "dir"))
        self.assertEqual(re.search(self.pattern, r"new -a file").groups(), ("new", "-a", None, "file", None))
        self.assertEqual(re.search(self.pattern, r"new -a file dir").groups(), ("new", "-a", None, "file", "dir"))
        self.assertEqual(re.search(self.pattern, r"new -a -v file").groups(), ("new", "-a", "-v", "file", None))
        self.assertEqual(re.search(self.pattern, r"new -a -v file dir").groups(), ("new", "-a", "-v", "file", "dir"))

    def test_read(self):
        self.assertEqual(re.search(self.pattern, r"read file").groups(), ("read", None, None, "file", None))
        self.assertEqual(re.search(self.pattern, r"read file dir").groups(), ("read", None, None, "file", "dir"))
        self.assertEqual(re.search(self.pattern, r"read -a file").groups(), ("read", "-a", None, "file", None))
        self.assertEqual(re.search(self.pattern, r"read -a file dir").groups(), ("read", "-a", None, "file", "dir"))
        self.assertEqual(re.search(self.pattern, r"read -a -v file").groups(), ("read", "-a", "-v", "file", None))
        self.assertEqual(re.search(self.pattern, r"read -a -v file dir").groups(), ("read", "-a", "-v", "file", "dir"))

    def test_del(self):
        self.assertEqual(re.search(self.pattern, r"del file").groups(), ("del", None, None, "file", None))
        self.assertEqual(re.search(self.pattern, r"del file dir").groups(), ("del", None, None, "file", "dir"))
        self.assertEqual(re.search(self.pattern, r"del . dir").groups(), ("del", None, None, ".", "dir"))


if __name__ == '__main__':
    unittest.main()