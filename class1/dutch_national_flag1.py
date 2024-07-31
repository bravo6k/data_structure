import unittest
# divide the array into two parts: elements less than or equal to the pivot, 
# and elements greater than the pivot. 
# This is often referred to as the "Lomuto partition scheme" and is commonly used in quicksort implementations.
# Time O(n)
def partition(arr, pivot):
    # Placeholder for the actual implementation
    p1, p2 = 0, 0
    while p2 < len(arr):
        if arr[p2] <= pivot:
            arr[p2], arr[p1] = arr[p1], arr[p2]
            p1+=1
        p2+=1
    return arr

import unittest

def partition(arr, pivot):
    p1, p2 = 0, 0
    while p2 < len(arr):
        if arr[p2] <= pivot:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
        p2 += 1
    return arr

class TestLomutoPartition(unittest.TestCase):
    def check_partition(self, original, pivot):
        partitioned = partition(original.copy(), pivot)
        pivot_index = len([x for x in partitioned if x <= pivot])
        
        # Check if all elements up to pivot_index are <= pivot
        self.assertTrue(all(x <= pivot for x in partitioned[:pivot_index]))
        
        # Check if all elements after pivot_index are > pivot
        self.assertTrue(all(x > pivot for x in partitioned[pivot_index:]))
        
        # Check if the partitioned array is a permutation of the original
        self.assertEqual(sorted(original), sorted(partitioned))

    def test_basic_case(self):
        arr = [2, 1, 3, 4, 5, 2, 3, 1]
        self.check_partition(arr, 3)

    def test_all_equal(self):
        arr = [2, 2, 2, 2, 2]
        self.check_partition(arr, 2)

    def test_already_partitioned(self):
        arr = [1, 2, 3, 4, 5, 6]
        self.check_partition(arr, 3)

    def test_reverse_order(self):
        arr = [5, 4, 3, 2, 1]
        self.check_partition(arr, 3)

    def test_all_less_equal_than_pivot(self):
        arr = [1, 2, 3, 4, 5]
        self.check_partition(arr, 5)

    def test_all_greater_than_pivot(self):
        arr = [6, 7, 8, 9, 10]
        self.check_partition(arr, 5)

    def test_empty_array(self):
        arr = []
        self.check_partition(arr, 3)

    def test_single_element(self):
        arr = [1]
        self.check_partition(arr, 1)

    def test_two_elements_sorted(self):
        arr = [1, 2]
        self.check_partition(arr, 1)

    def test_two_elements_unsorted(self):
        arr = [2, 1]
        self.check_partition(arr, 1)

    def test_with_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.check_partition(arr, 4)

    def test_large_array(self):
        arr = list(range(1000)) + list(range(1000, 0, -1))
        self.check_partition(arr, 500)

    def test_pivot_not_in_array(self):
        arr = [1, 3, 5, 7, 9]
        self.check_partition(arr, 4)

    def test_pivot_smallest(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        self.check_partition(arr, 1)

    def test_pivot_largest(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        self.check_partition(arr, 9)

if __name__ == '__main__':
    unittest.main()