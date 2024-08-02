def is_max_heap(arr, n, i):
    # If the current node is a leaf node, return True as leaf nodes are always heaps
    if i >= n:
        return True

    # Calculate the indices of the left and right children
    left = 2 * i + 1
    right = 2 * i + 2

    # Recursively check for left and right children
    is_left_heap = (left >= n or arr[i] >= arr[left]) and is_max_heap(arr, n, left)
    is_right_heap = (right >= n or arr[i] >= arr[right]) and is_max_heap(arr, n, right)

    # Return True if both left and right subtrees are heaps and the current node is greater than its children
    return is_left_heap and is_right_heap

def is_max_heap(arr):
    if not arr:
        return True
    return _ismax(arr, 0)

is_max_heap([100, 19, 36, 17, 3, 25, 1, 2, 7])
def test_max_heap():
    # 1. Valid max heap
    assert is_max_heap([100, 19, 36, 17, 3, 25, 1, 2, 7]) == True

    # 2. Another valid max heap
    assert is_max_heap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True

    # 3. Not a max heap (violates max heap property)
    assert is_max_heap([100, 19, 36, 17, 3, 25, 1, 2, 200]) == False

    # 4. Edge case: Single element (always a valid max heap)
    assert is_max_heap([1]) == True

    # 5. Edge case: Empty array (considered a valid max heap)
    assert is_max_heap([]) == True

    # 6. Edge case: Two elements, valid max heap
    assert is_max_heap([5, 3]) == True

    # 7. Edge case: Two elements, not a max heap
    assert is_max_heap([3, 5]) == False

    # 8. Large valid max heap
    large_heap = [100] + list(range(99, 0, -1))
    assert is_max_heap(large_heap) == True

    # 9. Large invalid max heap (one violation)
    large_invalid_heap = large_heap.copy()
    large_invalid_heap[-1] = 101
    assert is_max_heap(large_invalid_heap) == False

    # 10. Max heap with duplicate values
    assert is_max_heap([10, 10, 9, 9, 9, 8, 8, 7, 6]) == True

    # 11. Not a max heap (incomplete tree)
    assert is_max_heap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False

    print("All test cases passed!")

# Run the tests
test_max_heap()