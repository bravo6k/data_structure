def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

import unittest

class TestSelectionSort(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(selection_sort([5, 3, 8, 4, 2]), [2, 3, 4, 5, 8])
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Already sorted
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  # Reverse order

    def test_edge_cases(self):
        self.assertEqual(selection_sort([]), [])  # Empty list
        self.assertEqual(selection_sort([1]), [1])  # Single element list

    def test_with_duplicates(self):
        self.assertEqual(selection_sort([3, 3, 2, 1, 2]), [1, 2, 2, 3, 3])
        self.assertEqual(selection_sort([1, 2, 2, 1, 1]), [1, 1, 1, 2, 2])

    def test_large_list(self):
        large_list = list(range(1000, 0, -1))
        sorted_large_list = list(range(1, 1001))
        self.assertEqual(selection_sort(large_list), sorted_large_list)

    def test_longer_examples(self):
        longer_list = [i for i in range(10000, 0, -1)]
        sorted_longer_list = [i for i in range(1, 10001)]
        self.assertEqual(selection_sort(longer_list), sorted_longer_list)
        
        large_random_list = [99, 23, 4, 1, 8, 7, 0, 98, 45, 67, 56, 89, 12, 34, 76, 43, 21, 88, 9, 11]
        self.assertEqual(selection_sort(large_random_list), sorted(large_random_list))

if __name__ == '__main__':
    unittest.main()
