# Goal: To find the sum of the elements in an array
arr = [2,5,1,7,4,9]

#1. Using Built in Sum() fn
print(sum(arr))

#2. Using for Loop
total_sum = 0
for i in range(len(arr)):
    total_sum += arr[i]
print(total_sum)

#3. Using While loop
total_sum = 0
index = 0

while index < len(arr):
    total_sum += arr[index]
    index += 1 
print(total_sum)

#4. Recursion method
def sum_elem(arr):
    if not arr:
        return 0
    return arr[0] + sum_elem(arr[1:])
print(sum_elem(arr)) # calling fn