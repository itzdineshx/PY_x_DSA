# Collection: counter, namedtuple, deque, defaultdict

from collections import Counter, namedtuple, OrderedDict, deque

# Counter - for tracking iterables
# name = "aaaabbbbccccc"
# name_counter = Counter(name)
# print(name_counter.items())
# print(name_counter.keys())
# print(name_counter.values())

# namedtuple - key with agruments in tuple
# Pointer = namedtuple('Pointer', "x,y")
# points = Pointer(1,2)
# print(Pointer) #<class '__main__.Pointer'>
# print(points.x, points.y)

# orderDict - order of Dictionar
# dict = OrderedDict()
# dict['a'] = 2
# dict['b'] = 3
# print(dict)

queue = deque(['name','age','DOB']) 
print(queue)