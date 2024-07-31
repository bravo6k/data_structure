import unittest


def smaller_sum(arr):
    if arr:
        return _smaller_sum(arr, 0, len(arr) - 1)
    else:
        return 0


def _smaller_sum(arr, left, right):
    if left == right:
        return 0

    mid = left + ((right - left) >> 1)
    left_sum = _smaller_sum(arr, left, mid)
    right_sum = _smaller_sum(arr, mid + 1, right)
    sum = 0
    arr_copy = []
    left_idx, right_idx = left, mid + 1
    while left_idx <= mid and right_idx <= right:
        if arr[left_idx] < arr[right_idx]:
            sum += arr[left_idx] * (right - right_idx + 1)
            arr_copy.append(arr[left_idx])
            left_idx += 1
        else:
            arr_copy.append(arr[right_idx])
            right_idx += 1

    while left_idx <= mid:
        arr_copy.append(arr[left_idx])
        left_idx += 1

    while right_idx <= right:
        arr_copy.append(arr[right_idx])
        right_idx += 1

    for i, j in zip(range(len(arr_copy)), range(left, right + 1)):
        arr[j] = arr_copy[i]

    return sum + left_sum + right_sum


class TestSmallerSum(unittest.TestCase):
    def test_basic_case(self):
        arr = [1, 3, 4, 2, 5]
        self.assertEqual(smaller_sum(arr), 16)
        # Explanation: 0 + 1 + (1+3) + 1 + (1+3+4+2) = 16

    def test_sorted_ascending(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(smaller_sum(arr), 20)
        # Explanation: 0 + 1 + (1+2) + (1+2+3) + (1+2+3+4) = 20

    def test_sorted_descending(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(smaller_sum(arr), 0)
        # Explanation: No element has a smaller element to its left

    def test_all_same(self):
        arr = [3, 3, 3, 3, 3]
        self.assertEqual(smaller_sum(arr), 0)
        # Explanation: No element has a smaller element to its left

    def test_single_element(self):
        arr = [42]
        self.assertEqual(smaller_sum(arr), 0)
        # Explanation: Single element has no smaller sum

    def test_two_elements(self):
        arr = [5, 2]
        self.assertEqual(smaller_sum(arr), 0)
        # Explanation: No smaller elements to the left of any element

    def test_negative_numbers(self):
        arr = [-3, 1, -4, 2, -5]
        self.assertEqual(smaller_sum(arr), -9)
        # Explanation: 0 + (-3) + 0 + (1-3-4) + 0 = -9

    def test_large_numbers(self):
        arr = [1000, 100, 10000, 10, 100000]
        self.assertEqual(smaller_sum(arr), 12210)
        # Explanation: 0 + 0 + 1100 + 0 + 11110 = 12110

    def test_empty_array(self):
        arr = []
        self.assertEqual(smaller_sum(arr), 0)
        # Explanation: Empty array should return 0


if __name__ == "__main__":
    unittest.main()
