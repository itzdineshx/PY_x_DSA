# Goal: move the zeros to the end of array(without changing the order)

# 1. Brute Force
arr = [3,0,4,0,2,5,6]
n = len(arr)
i = 0
while i < n:
    if arr[i] == 0:
        arr.pop(i)
        arr.append(0)
        n -= 1
    else:
        i += 1
print(arr)

# 2. Two pointers
j = 0
for i in range(n):
    if arr[i] != 0: # check
        arr[j], arr[i] = arr[i], arr[j] #swap
        j += 1 # update
print(arr)