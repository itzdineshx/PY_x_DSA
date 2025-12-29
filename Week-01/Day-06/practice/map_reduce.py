# Lamba with Map, filter, Reduce
from functools import reduce

# a = [2,5,6,25,5]
# b = map(lambda x: x**2 ,a)
# print(f"Map {list(b)}")

# a = [2,5,6,25,5]
# b = filter(lambda x: x%2==0,a)
# print(f"Map {list(b)}")

a = [2,5,6,2,5,5]
b = reduce(lambda x,y : x*y, a)
print(b)
