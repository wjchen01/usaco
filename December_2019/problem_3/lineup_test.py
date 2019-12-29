import unittest
from lineup import merge_2, merge_list


class MyTestCase(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge_2(['Bessie', 'Blue'], ['Bessie', 'Buttercup']), [
                         ['Blue', 'Bessie', 'Buttercup']])
        self.assertEqual(merge_2(['A', 'B'], ['B', 'C']), [['A', 'B', 'C']])
        self.assertEqual(merge_2(['A', 'C'], ['B', 'C']), [['A', 'C', 'B']])
        self.assertEqual(merge_2(['A', 'B'], ['C', 'D']), [
                         ['A', 'B'], ['C', 'D']])
        self.assertEqual(merge_2(['A', 'B', 'C', 'D'], ['D', 'E', 'F', 'G']), [
                         ['A', 'B', 'C', 'D', 'E', 'F', 'G']])
        self.assertEqual(merge_2(['A', 'B', 'C', 'D'], ['A', 'E', 'F', 'G']), [
                         ['D', 'C', 'B', 'A', 'E', 'F', 'G']])

    def test_merge_list(self):
        self.assertEqual(merge_list([['Bessie', 'Blue'], ['Bessie', 'Buttercup']]), [
                         ['Blue', 'Bessie', 'Buttercup']])
        self.assertEqual(merge_list([['Beatrice', 'Sue'], ['Bessie', 'Blue'], [
                         'Bessie', 'Buttercup']]), [['Beatrice', 'Sue'], ['Blue', 'Bessie', 'Buttercup']])


if __name__ == '__main__':
    unittest.main()
