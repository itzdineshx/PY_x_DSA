# generator - special type of function that returns an iterator object

def sq_gen(num):
    for i in range(num):
        yield i**2 # yields -> pause -> resume

nums = sq_gen(122)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

# def inf_e values that are passed during the calling of the programseq():
#     result = 1
#     while True:
#         yield result
#         result += 2