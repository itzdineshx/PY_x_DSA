# To find the max sum in a given arr - Brute force
arr = [2, 1, 5, 1, 3, 2]
k = 3 # pair
n = len(arr)

window_sum = sum(arr[:k]) # pre computed max sum
max_sum = window_sum

for i in range(k, n):
    window_sum += arr[i]
    window_sum -= arr[i-k]
    max_sum = max(max_sum, window_sum)
print(max_sum)

"""
Complexity:
Time: O(n) - Single pass of arr
Space: O(1)
"""