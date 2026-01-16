# To find the max sum in a given arr - Brute force
arr = [2, 1, 5, 1, 3, 2]
k = 3 # pair
max_sum = 0

for i in range(len(arr) - k + 1):
    s = 0
    for j in range(i, i + k):
        s += arr[j]
    max_sum = max(max_sum, s)

print(max_sum)

"""
Time: O(nk)
Space: O(1)
"""