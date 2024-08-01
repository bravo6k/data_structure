import unittest

def dutch_national_flag(arr, pivot):
    p1, p2, p3 = 0, 0, len(arr) - 1
    while p2 < len(arr) and p3>=p2:
        if arr[p2] < pivot:
            arr[p2], arr[p1] = arr[p1], arr[p2]
            p1 += 1
            p2 += 1
        elif arr[p2] > pivot:
            arr[p2], arr[p3] = arr[p3], arr[p2]
            p3 -= 1
        else:
            p2 += 1
    return arr

print(dutch_national_flag([2, 5, 5, 3, 5, 2, 3, 4,3], 3))


class TestDutchNationalFlag(unittest.TestCase):
    def check_partition(self, original, pivot):
        arr = original.copy()
        dutch_national_flag(arr, pivot)
        
        # Find the boundaries of the three partitions
        left = 0
        while left < len(arr) and arr[left] < pivot:
            left += 1
        
        right = len(arr) - 1
        while right >= 0 and arr[right] > pivot:
            right -= 1
        
        # Check if all elements are correctly partitioned
        self.assertTrue(all(x < pivot for x in arr[:left]))
        self.assertTrue(all(x == pivot for x in arr[left:right+1]))
        self.assertTrue(all(x > pivot for x in arr[right+1:]))
        
        # Check if the partitioned array is a permutation of the original
        self.assertEqual(sorted(original), sorted(arr))

    def test_basic_case(self):
        arr = [2, 1, 3, 2, 5, 4, 2, 3]
        self.check_partition(arr, 3)

    def test_all_equal(self):
        arr = [2, 2, 2, 2, 2]
        self.check_partition(arr, 2)

    def test_already_partitioned(self):
        arr = [1, 1, 2, 2, 3, 3]
        self.check_partition(arr, 2)

    def test_reverse_order(self):
        arr = [5, 4, 3, 2, 1]
        self.check_partition(arr, 3)

    def test_all_less_than_pivot(self):
        arr = [1, 2, 3, 4, 5]
        self.check_partition(arr, 6)

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
        self.check_partition(arr, 2)

    def test_two_elements_unsorted(self):
        arr = [2, 1]
        self.check_partition(arr, 2)

    def test_with_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.check_partition(arr, 5)

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