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