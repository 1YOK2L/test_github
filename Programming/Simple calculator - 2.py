from math import *
from functools import reduce

def calculator(operation, *args):
    if operation == "+":
        return reduce(lambda total, value : total + value, args, 0)
    elif operation == "-":
        first_num = args[0]
        rest = reduce(lambda total, value : total + value, args[1:], 0)
        return first_num - rest
    elif operation == "*":
        return prod(args)
    elif operation == "/":
        first_num = args[0]
        rest = prod(args[1:])
        if first_num / rest % 1 == 0:
            return "%d" % (first_num / rest)
        else:
            return first_num / rest
print(calculator("+", 1, 2, 3))
print(calculator("-", 1, 2, 3, 4))
print(calculator("*", 1, 2, 3, 4, 5))
print(calculator("/", 10, 5))