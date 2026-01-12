# 4. Merge Sort - Divide -> Conquer -> Merge
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