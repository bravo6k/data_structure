def find_leftmost_index(arr, target):
    if arr:
        return _find_leftmost_index(arr, target, 0, len(arr)-1, -1)
    else:
        return -1

def _find_leftmost_index(arr, target, left, right, idx):
    if left > right:
        return idx
    
    mid = left + ((right - left)>>1)
    if arr[mid] >= target:
        idx = mid
        return _find_leftmost_index(arr, target, left, mid - 1, idx)
    else:
        return _find_leftmost_index(arr, target, mid+1, right, idx)
    


import unittest

class TestFindLeftmostIndex(unittest.TestCase):
    def test_found_cases(self):
        self.assertEqual(find_leftmost_index([1, 2, 2, 2, 3, 4, 5], 2), 1)
        self.assertEqual(find_leftmost_index([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(find_leftmost_index([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(find_leftmost_index([1, 2, 3, 4, 5], 4), 3)
        self.assertEqual(find_leftmost_index([1, 2, 3, 4, 5], 5), 4)

    def test_not_found_cases(self):
        self.assertEqual(find_leftmost_index([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(find_leftmost_index([10, 20, 30, 40, 50], 55), -1)
        self.assertEqual(find_leftmost_index([10, 20, 30, 40, 50], 0), 0)
        self.assertEqual(find_leftmost_index([], 3), -1)

    def test_edge_cases(self):
        self.assertEqual(find_leftmost_index([1], 1), 0)  # Single element list, target present
        self.assertEqual(find_leftmost_index([1], 2), -1)  # Single element list, target not present
        self.assertEqual(find_leftmost_index([1, 1, 1, 1, 1], 1), 0)  # All elements same and equal to target

    def test_large_list(self):
        large_list = list(range(1, 10001))
        self.assertEqual(find_leftmost_index(large_list, 5000), 4999)
        self.assertEqual(find_leftmost_index(large_list, 10000), 9999)
        self.assertEqual(find_leftmost_index(large_list, 1), 0)

if __name__ == '__main__':
    unittest.main()
