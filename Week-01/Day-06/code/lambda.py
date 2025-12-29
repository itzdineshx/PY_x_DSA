# Lambda functions - anonymous functions means that the function is without a name
"""
lambda arguments : expression
"""

# def add(x):
#     return x + 4

add = lambda x : x + 4
print(add(x=4))

s1 = 'dkverse'
s2 = lambda func: func.upper()
print(s2(s1))

n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))   

li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i(), end=" ")