# itertools module is a collection of tools for handling iterators
from itertools import product, permutations, combinations, accumulate, groupby, count
import operator

# a = [2,4]
# b = [5,3]
# prod = product(a,b, repeat=1)
# print(list(prod))

# a = [2,45,3]
# perm = permutations(a)
# print(list(perm))

# a = [3, 4, 3, 5]
# comb = combinations(a,2)
# print(list(comb))

# a = [3, 4, 3, 5]
# acc = accumulate(a, func=operator.add)
# print(list(acc))


for number in count(start=1, step=2):
    if number > 10:
        break
    print(number)  # print statement