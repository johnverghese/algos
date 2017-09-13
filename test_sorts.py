import unittest

import mergesort
import quicksort
import insertion_sort

class TestInsertion(unittest.TestCase):
    def setUp(self):
        self.a = [9, 4, 7, 3, 5, 8, 10 ,1]
        self.b = ["The", "sun", "is", "sinking", "in", "the", "west"]

    def tearDown(self):
        pass

    def test_insertion(self):
        self.assertEqual(sorted(self.a), insertion_sort.insertion_sort(self.a))
        self.assertEqual(sorted(self.b), insertion_sort.insertion_sort(self.b))


class TestMerge(unittest.TestCase):
    def setUp(self):
        self.a = [9, 4, 7, 3, 5, 8, 10 ,1]
        self.b = ["The", "sun", "is", "sinking", "in", "the", "west"]

    def tearDown(self):
        pass

    def test_merge(self):
        self.assertEqual(sorted(self.a), mergesort.merge_sort(self.a))
        self.assertEqual(sorted(self.b), mergesort.merge_sort(self.b))

class TestQuick(unittest.TestCase):
    def setUp(self):
        self.a = [9, 4, 7, 3, 5, 8, 10 ,1]
        self.b = ["The", "sun", "is", "sinking", "in", "the", "west"]

    def tearDown(self):
        pass

    def test_quick(self):
        self.assertEqual(sorted(self.a), quicksort.quicksort(self.a))
        self.assertEqual(sorted(self.b), quicksort.quicksort(self.b))




if __name__ == '__main__':
    unittest.main()


