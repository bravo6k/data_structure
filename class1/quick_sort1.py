def quicksort(arr):
    # Quicksort implementation goes here
    if arr:
        return _quicksort(arr,len(arr)-1)
    else:
        return arr
    
def _quicksort(arr, target_idx, left, right):
    if left == right:
        return
    target_num = arr[target_idx]
    p0, p1 = 0, 0
    while p1 <= len(arr) - 1:
        if arr[p1] < target_num:
            arr[p1], arr[p0] = arr[p0], arr[p1]
            p0+=1
        


# Test cases
def test_quicksort():
    # 1. Normal case: Unsorted array
    assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    # 2. Edge case: Empty array
    assert quicksort([]) == []

    # 3. Edge case: Array with one element
    assert quicksort([1]) == [1]

    # 4. Edge case: Already sorted array
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # 5. Edge case: Reverse sorted array
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # 6. Case: Array with duplicate elements
    assert quicksort([3, 3, 3, 1, 1, 2, 2]) == [1, 1, 2, 2, 3, 3, 3]

    # 7. Case: Array with negative numbers
    assert quicksort([-3, 5, -1, 0, 4, -2]) == [-3, -2, -1, 0, 4, 5]

    # 8. Case: Array with floating-point numbers
    assert quicksort([3.14, 2.71, 1.41, 0.58]) == [0.58, 1.41, 2.71, 3.14]

    # 9. Edge case: Array with all elements the same
    assert quicksort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]

    # 10. Case: Large array (testing performance)
    import random
    large_array = [random.randint(1, 1000) for _ in range(10000)]
    assert quicksort(large_array) == sorted(large_array)

    print("All test cases passed!")

# Run the tests
test_quicksort()