import unittest


def count_inversion_pairs(arr):
    # Placeholder for the actual implementation
    if arr:
        return _count(arr, 0, len(arr) - 1)
    else:
        return 0


def _count(arr, left, right):
    if left == right:
        return 0

    mid = left + ((right - left) >> 1)
    left_count = _count(arr, left, mid)
    right_count = _count(arr, mid + 1, right)
    count = 0
    left_idx, right_idx = left, mid + 1
    arr_copy = []
    while left_idx <= mid and right_idx <= right:
        if arr[left_idx] <= arr[right_idx]:
            arr_copy.append(arr[right_idx])
            right_idx += 1
        else:
            arr_copy.append(arr[left_idx])
            left_idx += 1
            count += right - right_idx + 1

    while left_idx <= mid:
        arr_copy.append(arr[left_idx])
        left_idx += 1

    while right_idx <= right:
        arr_copy.append(arr[right_idx])
        right_idx += 1

    for i, j in zip(range(len(arr_copy)), range(left, right + 1)):
        arr[j] = arr_copy[i]

    return count + left_count + right_count


class TestInversionPairs(unittest.TestCase):
    def test_sorted_ascending(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(count_inversion_pairs(arr), 0)
        # Explanation: No inversions in a sorted array

    def test_sorted_descending(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(count_inversion_pairs(arr), 10)
        # Explanation: Every pair is an inversion

    def test_mixed_order(self):
        arr = [2, 4, 1, 3, 5]
        self.assertEqual(count_inversion_pairs(arr), 3)
        # Explanation: (2,1), (4,1), (4,3) are inversions

    def test_duplicate_elements(self):
        arr = [4, 4, 2, 3, 1]
        self.assertEqual(count_inversion_pairs(arr), 8)
        # Explanation: (4,2), (4,3), (4,1), (4,2), (4,3), (4,1), (2,1)

    def test_single_element(self):
        arr = [42]
        self.assertEqual(count_inversion_pairs(arr), 0)
        # Explanation: Single element has no inversions

    def test_two_elements_no_inversion(self):
        arr = [1, 2]
        self.assertEqual(count_inversion_pairs(arr), 0)
        # Explanation: No inversion in [1, 2]

    def test_two_elements_with_inversion(self):
        arr = [2, 1]
        self.assertEqual(count_inversion_pairs(arr), 1)
        # Explanation: One inversion in [2, 1]

    def test_negative_numbers(self):
        arr = [-3, 1, -4, 2, -5]
        self.assertEqual(count_inversion_pairs(arr), 6)
        # Explanation: (-3,-4), (-3,-5), (1,-4), (1,-5), (2,-5)

    def test_large_numbers(self):
        arr = [1000, 100, 10000, 10, 100000]
        self.assertEqual(count_inversion_pairs(arr), 4)
        # Explanation: (1000,100), (1000,10), (10000,10)

    def test_empty_array(self):
        arr = []
        self.assertEqual(count_inversion_pairs(arr), 0)
        # Explanation: Empty array has no inversions

    def test_large_array(self):
        arr = list(range(1000, 0, -1))  # [1000, 999, ..., 2, 1]
        self.assertEqual(count_inversion_pairs(arr), 499500)
        # Explanation: Sum of 1 to 999 = 999*1000/2 = 499500


if __name__ == "__main__":
    unittest.main()
