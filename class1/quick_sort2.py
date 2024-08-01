def quicksort(arr):
    # Quicksort implementation goes here
    if arr:
        _quicksort(arr, 0, len(arr)-1)
    return arr
    
def _quicksort(arr, left, right):
    if left >= right:
        return
    p0, p1, p2 = left, left, right
    target = arr[right]
    while p1 <=right or p1 <= p2:
        if arr[p1] < target:
            arr[p1], arr[p0] = arr[p0], arr[p1]
            p0 += 1
            p1 += 1
        elif arr[p1] > target:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p2 -= 1
    arr[right], arr[p2+1] = arr[p0], arr[p2+1]


    


        


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