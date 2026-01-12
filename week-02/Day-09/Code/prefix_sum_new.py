# prefix sum array (new Array)
arr = [1,3,5,2,7]
n = len(arr)
s_arr = [0] * n # [5]
s_arr[0] = arr[0] # [1,0,0,0,0]

for i in range(1,n):
    s_arr[i] = arr[i] + s_arr[i-1] # 2nd elem + 1st elem
print(arr)
print(s_arr)