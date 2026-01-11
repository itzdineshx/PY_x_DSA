"""
Problem Name : Largest Element in an array
Type : Traversal
"""

# Brute Force
"""
Algorithm:
1. Sort the array to ascending order
2. Return the last(n-1) Element of an array
"""

# arr1 = [2,4,3,2,1]
# sort_array = sorted(arr1) #[1,2,2,3,4]

# print(f"The Largest element is: {sort_array[-1]}") # The Largest element is: 4

"""
Time Complexity:
----------------
O(n log n) - Sorting

Space Complexity:
-----------------
O(n) – Extra Array = Extra Space
"""

# Optimized Solution
"""
Algorithm:
1. Initialize a pointer at index of 0
2. store the arr[0] in a variable
3. Traverse through each array of elements
4. Compare with each and every element and update the largest
5. Return the Largest element

"""
arr1 = [2,4,3,2,1]

largest = arr1[0]

for i in range(1, len(arr1)): # arr[1 -> -1]
    if arr1[i] > largest:
        largest = arr1[i] # Update the largest element
        
print(f"The Largest element is: {largest}") # The Largest element is: 4
"""
Time Complexity:
----------------
O(n) – single traversal

Space Complexity:
-----------------
O(1) – in-place modification
"""