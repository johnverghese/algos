import unittest

import mergesort

class TestMerge(unittest.TestCase):
    def setUp(self):
        self.a = [9, 4, 7, 3, 5, 8, 10 ,1]

    def tearDown(self):
        pass

    def test_merge(self):
        self.assertEqual(sorted(self.a), mergesort.merge_sort(self.a))

if __name__ == '__main__':
    unittest.main()


