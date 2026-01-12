# 1. Selection Sort - Select -> Swap -> Sort
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