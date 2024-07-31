# only one number occur odd times
def find_unique_number(arr):
    b = 0
    for i in arr:
        b ^= i
    return b

import unittest

class TestFindUniqueNumber(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(find_unique_number([2, 3, 5, 4, 5, 3, 4]), 2)
        self.assertEqual(find_unique_number([1, 1, 2, 2, 3]), 3)
        self.assertEqual(find_unique_number([0, 1, 0]), 1)

    def test_edge_cases(self):
        self.assertEqual(find_unique_number([1]), 1)  # Single element
        self.assertEqual(find_unique_number([-1, -1, 2]), 2)  # Includes negative numbers
        self.assertEqual(find_unique_number([10, 10, -5, -5, 3]), 3)  # Mixed positive and negative

    def test_large_list(self):
        large_list = list(range(1, 100001)) + list(range(1, 100001)) + [100001]
        self.assertEqual(find_unique_number(large_list), 100001)

    def test_longer_examples(self):
        longer_list = [i for i in range(1, 10001)] * 2 + [10001]
        self.assertEqual(find_unique_number(longer_list), 10001)

if __name__ == '__main__':
    unittest.main()
