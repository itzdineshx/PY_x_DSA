# Goal: To found the Count of the number of elements in a list
arr = [12,5,1,5,2]

#1. Using the len() built in 
print(len(arr))

#2. Using the for loop
cnt = 0
for i in range(len(arr)):
    cnt += 1
print(cnt)

#3. While loop
cnt2 = 0
i = 0
n = len(arr)
while i < n:
    cnt2 += 1
    i += 1
print(cnt2)

#4. Recursion method
def cnt_elements(arr):
    if not arr:
        return 0
    return 1 + cnt_elements(arr[1:])
print(cnt_elements(arr)) # calling fn
