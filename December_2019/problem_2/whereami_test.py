import unittest
from whereami import is_unique

class MyTestCase(unittest.TestCase):
    def test_is_unique(self):
        #self.assertFalse(is_unique(1, "ABCDABC"))
        #self.assertFalse(is_unique(2, "ABCDABC"))
        #self.assertFalse(is_unique(3, "ABCDABC"))
        #self.assertTrue(is_unique(4, "ABCDABC"))
        self.assertFalse(is_unique(3, "ABCDECDE"))
        self.assertTrue(is_unique(4, "ABCDECDE"))


if __name__ == '__main__':
    unittest.main()
