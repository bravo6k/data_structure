def merge_sort(arr):
    if arr:
        _merge_sort(arr, 0, len(arr) - 1)
        return arr
    else:
        return arr


def _merge_sort(arr, left, right):
    if left == right:
        return

    mid = left + ((right - left) >> 1)
    _merge_sort(arr, left, mid)
    _merge_sort(arr, mid + 1, right)

    arr_copy = []
    idx_left, idx_right = left, mid + 1
    while idx_left <= mid and idx_right <= right:
        if arr[idx_left] <= arr[idx_right]:
            arr_copy.append(arr[idx_left])
            idx_left += 1
        else:
            arr_copy.append(arr[idx_right])
            idx_right += 1

    while idx_left <= mid:
        arr_copy.append(arr[idx_left])
        idx_left += 1

    while idx_right <= right:
        arr_copy.append(arr[idx_right])
        idx_right += 1

    for i, j in zip(range(len(arr_copy)), range(left, right + 1, 1)):
        arr[j] = arr_copy[i]


import unittest


class TestMergeSort(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(merge_sort([5, 3, 8, 4, 2]), [2, 3, 4, 5, 8])
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Already sorted
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  # Reverse order

    def test_edge_cases(self):
        self.assertEqual(merge_sort([]), [])  # Empty list
        self.assertEqual(merge_sort([1]), [1])  # Single element list

    def test_with_duplicates(self):
        self.assertEqual(merge_sort([3, 3, 2, 1, 2]), [1, 2, 2, 3, 3])
        self.assertEqual(merge_sort([1, 2, 2, 1, 1]), [1, 1, 1, 2, 2])

    def test_large_list(self):
        large_list = list(range(1000, 0, -1))
        sorted_large_list = list(range(1, 1001))
        self.assertEqual(merge_sort(large_list), sorted_large_list)

    def test_longer_examples(self):
        longer_list = [i for i in range(10000, 0, -1)]
        sorted_longer_list = [i for i in range(1, 10001)]
        self.assertEqual(merge_sort(longer_list), sorted_longer_list)

        large_random_list = [
            99,
            23,
            4,
            1,
            8,
            7,
            0,
            98,
            45,
            67,
            56,
            89,
            12,
            34,
            76,
            43,
            21,
            88,
            9,
            11,
        ]
        self.assertEqual(merge_sort(large_random_list), sorted(large_random_list))


import random


def generate_random_array(
    min_length=1, max_length=1000, min_value=-1000, max_value=1000
):
    """Generate a random array with random length and random integer elements."""
    length = random.randint(min_length, max_length)
    return [random.randint(min_value, max_value) for _ in range(length)]


def your_sort_method(arr):
    """
    Replace this function with your own sorting method.
    This is just a placeholder that uses Python's built-in sort.
    """
    return sorted(arr)


def test_sort_method(your_sort_method, num_tests=5000):
    for i in range(num_tests):
        # Generate a random array
        test_array = generate_random_array()

        # Create copies for sorting
        your_sorted = test_array.copy()
        python_sorted = test_array.copy()

        # Sort using both methods
        your_result = your_sort_method(your_sorted)
        python_result = sorted(python_sorted)

        # Compare results
        if your_result == python_result:
            print(f"Test {i+1}: Passed")
        else:
            print(f"Test {i+1}: Failed")
            print("Original array:", test_array)
            print("Your result:   ", your_result)
            print("Correct result:", python_result)
            return False  # Stop testing if a test fails

    print("All tests passed successfully!")
    return True


if __name__ == "__main__":
    # unittest.main()
    test_sort_method(merge_sort)
