from math import *

def calculator(operation, *args):
    if operation == "+":
        return sum(args)
    elif operation == "-":
        first_num = args[0]
        rest = sum(args[1:])
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