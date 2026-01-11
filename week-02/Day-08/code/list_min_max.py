# Goal: To Find the min and max of the given list

arr = [5,6,7,1,3,3]
max_elem = arr[0]
min_elem = arr[0]

# Finding the max Element
#1. Using the max() in built fn
print(max(arr))

#2. using the for loop(index Based)
max_elem = arr[0]
for i in range(len(arr)):
    if arr[i] > max_elem:
        max_elem = arr[i]
print(max_elem)

#3. using the for loop(val Based)
for x in arr:
    if x > max_elem:
        max_elem = x

print(max_elem)

#4. Using the While loop
i = 0
n = len(arr)

while i < n:
    if arr[i] > max_elem:
        max_elem = arr[i]
    i += 1
print(max_elem)

#5. Using enumerate()
for idx, val in enumerate(arr):
    if val > max_elem:
        max_elem = val
print(max_elem)

#6. Using Sort() - but more complexeity
arr.sort()
print(arr[-1])


# Finding the min Element
#1. Using the min() in built fn
print(min(arr))

#2. using the for loop(index Based)
min_elem = arr[0]
for i in range(len(arr)):
    if arr[i] < min_elem:
        min_elem = arr[i]
print(min_elem)

#3. using the for loop(val Based)
for x in arr:
    if x < min_elem:
        min_elem = x

print(min_elem)


#4. Using the While loop
i = 0
n = len(arr)
while i < n:
    if arr[i] <= min_elem:
        min_elem = arr[i]
    i += 1
print(min_elem)

#5. Using enumerate()
for idx, val in enumerate(arr):
    if val < min_elem:
        min_elem = val
print(min_elem)

#6. Using Sort() - but more complexeity
arr.sort()
print(arr[0])