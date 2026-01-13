# check if a pair of sums is same as target - Two Pointer
arr = [2,3,6,1,6]
targ = 7
arr.sort()
left ,right= 0 , len(arr) -1 # first, last

found = False
while left < right:
    s = arr[left] + arr[right]
    if s == targ:
        found = True
        break
    elif s < targ:
        left += 1
    else:
        right -= 1
print(found)