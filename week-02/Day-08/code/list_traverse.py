# Goal: To Traverse all the elements in an array
arr = [2,6,2,8,5,3]

#1. Using for loop(index Based)
for i in range(len(arr)):
    print(arr[i])

#2. Using for loop(Value Based)
for num in arr:
    print(num)

#3. Using While loop
i = 0
idx = 0
n = len(arr)
while i < n:
    print(arr[i])
    i += 1

#4. Using enumerate()
for idx, val in enumerate(arr):
    print(idx, val)

#5. Reverse Traversal
for i in range(len(arr)-1, -1, -1):
    print(arr[i])

#6. 2D Traversal
matrix = [[1,2,3], [4,5,6]]
for row in matrix:
    for col in matrix:
        print(val)