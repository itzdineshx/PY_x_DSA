# 2. Bubble Sort - Comapare -> Max -> Adjacent Swap
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