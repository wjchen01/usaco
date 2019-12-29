import unittest
# from gymnastics import small_list, cro_list
from .gymnastics import small_list, cro_list

class MyTestCase(unittest.TestCase):
    def test_small_list(self):
        self.assertEqual(small_list([4, 1, 2, 3]), [[4, 1], [4, 2], [4, 3]])
        self.assertEqual(small_list([5, 4, 1, 2, 3]), [[5, 4], [5, 1], [5, 2], [5, 3]])

    def test_cro_list(self):
        self.assertEqual(cro_list([4, 1, 2, 3]), [[4, 1], [4, 2], [4, 3], [1, 2], [1, 3], [2, 3]])
        self.assertEqual(cro_list([5, 4, 1, 2, 3]), [[5, 4], [5, 1], [5, 2], [5, 3], [4, 1], [4, 2], [4, 3], [1, 2], [1, 3], [2, 3]])

    def test_count(self):
        test_list = [[4, 1], [4, 2], [4, 3], [1, 2], [4, 1], [1, 3], [2, 3]]
        self.assertEqual(test_list.count([4, 1]), 2)

if __name__ == '__main__':
    unittest.main()
