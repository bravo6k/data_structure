def bubble_sort(arr):
    e = len(arr)
    while e > 1:
        for i in range(e-1):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
        e -= 1
    return arr

import unittest

class TestBubbleSort(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(bubble_sort([5, 3, 8, 4, 2]), [2, 3, 4, 5, 8])
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Already sorted
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  # Reverse order

    def test_edge_cases(self):
        self.assertEqual(bubble_sort([]), [])  # Empty list
        self.assertEqual(bubble_sort([1]), [1])  # Single element list

    def test_with_duplicates(self):
        self.assertEqual(bubble_sort([3, 3, 2, 1, 2]), [1, 2, 2, 3, 3])
        self.assertEqual(bubble_sort([1, 2, 2, 1, 1]), [1, 1, 1, 2, 2])

    def test_large_list(self):
        large_list = list(range(1000, 0, -1))
        sorted_large_list = list(range(1, 1001))
        self.assertEqual(bubble_sort(large_list), sorted_large_list)

    def test_longer_examples(self):
        longer_list = [i for i in range(10000, 0, -1)]
        sorted_longer_list = [i for i in range(1, 10001)]
        self.assertEqual(bubble_sort(longer_list), sorted_longer_list)
        
        large_random_list = [99, 23, 4, 1, 8, 7, 0, 98, 45, 67, 56, 89, 12, 34, 76, 43, 21, 88, 9, 11]
        self.assertEqual(bubble_sort(large_random_list), sorted(large_random_list))

if __name__ == '__main__':
    unittest.main()