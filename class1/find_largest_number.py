def find_largest_number(arr):
    if arr:
        return _find_number(arr, 0, len(arr)-1)
    else:
        return None

def _find_number(arr, left, right):
    if left == right:
        return arr[left]
    
    mid = left + ((right - left)>>1)
    left_max = _find_number(arr, left, mid)
    right_max = _find_number(arr, mid+1, right)
    return max(left_max, right_max)

import unittest

class TestFindLargestNumber(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(find_largest_number([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_largest_number([10, 20, 30, 40, 50]), 50)

    def test_negative_numbers(self):
        self.assertEqual(find_largest_number([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(find_largest_number([-10, -20, -30, -40, -50]), -10)

    def test_mixed_numbers(self):
        self.assertEqual(find_largest_number([1, -2, 3, -4, 5]), 5)
        self.assertEqual(find_largest_number([-1, 2, -3, 4, -5]), 4)

    def test_single_element(self):
        self.assertEqual(find_largest_number([1]), 1)
        self.assertEqual(find_largest_number([-1]), -1)

    def test_identical_elements(self):
        self.assertEqual(find_largest_number([5, 5, 5, 5, 5]), 5)
        self.assertEqual(find_largest_number([-1, -1, -1, -1]), -1)

    def test_empty_list(self):
        self.assertEqual(find_largest_number([]), None)

    def test_large_numbers(self):
        self.assertEqual(find_largest_number([1e10, 1e12, 1e11, 1e9]), 1e12)
        self.assertEqual(find_largest_number([-1e10, -1e12, -1e11, -1e9]), -1e9)

    def test_floats(self):
        self.assertEqual(find_largest_number([1.1, 2.2, 3.3, 4.4, 5.5]), 5.5)
        self.assertEqual(find_largest_number([-1.1, -2.2, -3.3, -4.4, -5.5]), -1.1)

    def test_mixed_int_and_float(self):
        self.assertEqual(find_largest_number([1, 2.2, 3, 4.4, 5]), 5)
        self.assertEqual(find_largest_number([-1, -2.2, -3, -4.4, -5]), -1)

    def test_large_list(self):
        large_list = list(range(1000000))
        self.assertEqual(find_largest_number(large_list), 999999)

if __name__ == '__main__':
    unittest.main()


