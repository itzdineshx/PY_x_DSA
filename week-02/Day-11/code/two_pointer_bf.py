# check if a pair of sums is same as target - Brute Force
arr = [2,3,6,1,6]
targ = -2
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == targ: # 2+3 == -2?
            print(True) 
print(False)