# find num in ordered list
def binary_search(arr, target):
    if arr:
        return _binary_search(arr, target, 0, len(arr)-1)
    else:
        return -1

def _binary_search(arr, target, left, right):
    if left > right:
        return -1

    mid = left + ((right-left)>>1)
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return _binary_search(arr, target,mid+1, right)
    else:
        return _binary_search(arr, target,left, mid - 1)



import unittest

class TestBinarySearch(unittest.TestCase):
    def test_found_cases(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 10), 0)
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 50), 4)

    def test_not_found_cases(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 15), -1)
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 0), -1)

    def test_edge_cases(self):
        self.assertEqual(binary_search([], 1), -1)  # Empty list
        self.assertEqual(binary_search([1], 1), 0)  # Single element list, target present
        self.assertEqual(binary_search([1], 2), -1)  # Single element list, target not present

    def test_large_list(self):
        large_list = list(range(1, 10001))
        self.assertEqual(binary_search(large_list, 5000), 4999)
        self.assertEqual(binary_search(large_list, 10000), 9999)
        self.assertEqual(binary_search(large_list, 1), 0)

if __name__ == '__main__':
    unittest.main()
