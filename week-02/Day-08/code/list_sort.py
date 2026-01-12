# Goal: To Sort the array

arr = [13,24,52,20,9]

#1. Using the built in Sort()
arr.sort()
print(arr)

#2. Using the sorted() Method
print(sorted(arr, reverse=False))

#3. Selection Sort - Select -> Swap -> Sort
"""
Algorithm:
1. Traverse through the array (n -> n-1)
2. Find the Smallest element in the array
3. Then:
    - Compare with the first element of an array (pointer(arr[i]) < min)
    - If the pointer < min -> Swap the elements with positions
    - If the pointer > min -> No changes
    - else -> there is only one element or none
4. Move the pointer to the next element and continue comparison(arr[i+1] < next min)
    - yes = swap
    - no = remain and next
5. Loop untils the end and return the sorted array
"""

arr = [13,24,52,20,9]
for i in range(len(arr)-1): #1 Traverse
    mini = i #2 minimum
    for j in range(i, len(arr)): #3 Compare
        if arr[j] < arr[mini]:
            mini = j
    arr[i], arr[mini] = arr[mini], arr[i] #4 Swap
print(arr) #5 return Sorted

"""
Complexeity:
Time: O(n^2)
Space: O(1)
"""

#4. Bubble Sort - Comapare -> Max -> Adjacent Swap
"""
Algorithm:
1. Traverse through the array (n -> n-1)
2. Then:
    - Compare with i`th element and i+1`th element 
    - If i`th > i+1`th -> swap them
    - o.w traverse through next pairs(i+1, i+2)
3. Continue pair Swapping until the max reaches the end
4. Loop again and return the sorted array
"""

arr = [13,24,52,20,9]
for i in range(len(arr)): #1. Traverse
    swapped = False
    for j in range(0, len(arr)-1): #2. Compare
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j] #3. Swap
            swapped = True
    if not swapped:
        break
print(arr) #4. Return

"""
Complexeity:
Time: O(n^2) - worst, Average; O(n) - Best
Space: O(1)
"""

#5. Insertion Sort - Select -> compare -> Shift(left)
"""
Algorithm:
1.consider the first element as sorted
2. Traverse through the array of (i=1 -> n-1):
    - Store the curr element as key
    - Compare the key with the elements in the sorted portion
    - Shift all elements greater than the key 
3. Insert the key into its correct sorted position.
4. return the arr
"""

# Approach 1: key Based
arr = [13,24,52,20,9]
for i in range(1, len(arr)): # 1 -> n-1 (0 - sorted)
    key = arr[i] #2. Key
    j = i - 1

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1 # shift towards left
        arr[j + 1] = key #3. Insert -> indx
print(arr)

# Approach 2: Val Based
for i in range(1, len(arr)):
    j = i 
    while j > 0 and arr[j-1] > arr[j]: # py allows [-1]
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1
print(arr)

"""
Complexeity:
Time: O(n^2) - worst, Average; O(n) - Best
Space: O(1)
"""

#6. Merge Sort - Divide -> Conquer -> Merge
"""
Algorithm:
1. Find the len of array
2. Make them split into two by Recursion
3. Split until it becomes a single element
4. Now Sort and merge them
5. Then Compare the x`th index of both arrays
    - If i`th > j`th ? append(j)
    - o.w append(i)
    - Then move the pointers
6. Return the Sorted Array
"""

def merge_sort(arr):
    if len(arr) > 1:
    # Split the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both val
        merge_sort(left_half) # sort left half
        merge_sort(right_half) # sort Right half

        # Merge the sorted vals
        i = j = k = 0

        # store data in temp arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]: # i < j?
                arr[k] = left_half[i] # temp arr
                i += 1 # increase pointer pos
            else:
                arr[k] = right_half[j] # temp arr
                j += 1 # increase pointer pos
            k += 1

        # Add Remaining elements
        # 1. In left Half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # 2. In Right Half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

arr = [13,24,52,20,9]
print(merge_sort(arr))

"""
Complexeity:
Time Complexity: O(n*log(n)) - partition
Space: O(n) - Auxilary space
"""

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

def partition(arr, low, high):
    pivot = arr[high]          # Choose last element as pivot
    i = low - 1                # Pointer for smaller elements

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