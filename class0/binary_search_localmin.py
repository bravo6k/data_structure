def find_local_minimum(arr):
    if arr:
        n = len(arr)
    
        # Edge cases
        if n == 1:
            return 0
        if arr[0] < arr[1]:
            return 0
        if arr[n-1] < arr[n-2]:
            return n-1
        else:
            return _find_local_minimum(arr, 0, len(arr) - 1)
    else:
        return -1


def _find_local_minimum(arr, left, right):
    if left > right:
        return -1
    
    mid = left + ((right - left)>>1)

    if arr[mid] < arr[mid-1] and arr[mid] < arr[mid+1]:
        return mid
    elif arr[mid] < arr[mid-1]:
        return _find_local_minimum(arr, mid+1, right)
    elif arr[mid] >= arr[mid-1]:
        return _find_local_minimum(arr, left, mid-1)


import unittest

class TestFindLocalMinimum(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(find_local_minimum([1]), 0)  # Single element list
        self.assertEqual(find_local_minimum([1, 2]), 0)  # Two elements, first is local minimum
        self.assertEqual(find_local_minimum([2, 1]), 1)  # Two elements, second is local minimum

    def test_boundary_cases(self):
        self.assertEqual(find_local_minimum([1, 2, 3]), 0)  # First element is local minimum
        self.assertEqual(find_local_minimum([3, 2, 1]), 2)  # Last element is local minimum

    def test_middle_cases(self):
        self.assertEqual(find_local_minimum([4, 3, 2, 1, 2, 3, 4]), 3)  # Middle element is local minimum
        self.assertEqual(find_local_minimum([10, 5, 6, 4, 3, 7, 8, 9]), 4)  # Element 3 is local minimum

    def test_multiple_local_minima(self):
        local_min_index = find_local_minimum([5, 1, 4, 6, 3, 7, 2])
        self.assertIn(local_min_index, [1, 4, 6])  # There are multiple local minima

    def test_large_list(self):
        large_list = list(range(1000, 0, -1))
        self.assertEqual(find_local_minimum(large_list), 999)  # Last element is local minimum
        large_list = list(range(1, 1001)) + list(range(1000, 0, -1))
        self.assertEqual(find_local_minimum(large_list), 0)  # First element is local minimum
        large_list = list(range(1001, 1, -1)) + list(range(1000))
        self.assertEqual(find_local_minimum(large_list), 1000)  # Mid element is local minimum

if __name__ == '__main__':
    unittest.main()
