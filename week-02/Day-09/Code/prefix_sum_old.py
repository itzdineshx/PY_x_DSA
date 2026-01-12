# prefix sum array (With in Array)
arr = [1,3,5,2,7]
n = len(arr)

for i in range(1,n):
    arr[i] += arr[i-1]
print(arr)


"""
Time Complexity: O(n)
Auxiliary Space: O(n)
"""