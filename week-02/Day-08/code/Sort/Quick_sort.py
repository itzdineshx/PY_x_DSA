# 6. Quick Sort – Pick Pivot → Partition → Recursion

"""
Algorithm:
----------
1. Choose a pivot element (last, first, middle).
2. Partition the array such that:
   - Elements <= pivot -> left.
   - Elements >=  pivot -> right.
   - The pivot is placed in its correct sorted position.
3. Recursively apply Quick Sort to the left subarray.
4. Recursively apply Quick Sort to the right subarray.
5. Continue until subarrays have size 0 or 1.
6. Return the sorted Array
"""
arr = [9, 13, 20, 24, 52]
def partition(arr, low, high):
    pivot = arr[high]          # Pivot Element
    i = low - 1                # Pointer

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)   # Left subarray
        quick_sort(arr, p + 1, high)  # Right subarray

quick_sort(arr, 0, len(arr) - 1)
print(arr)
"""
Time Complexity:  O(n log n) - Best, Average
O(n²) - Worst Case:
Space Complexity: O(log n) – recursion stack
"""