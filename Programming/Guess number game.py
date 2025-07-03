from random import *

result = randint(1, 10)

x = input("Guess a number: ")
while x != result:
    if x.isnumeric() or (x[0] == "-" and x[1:].isnumeric()):
        x = int(x)
        if x > result:
            print("Too high")
        elif x < result:
            print("Too low")
        elif x == result:
            print("Yes! The correct answer is", result)
            break
        x = input("Guess a number: ")
    else:
        print("Invalid input")
        x = input("Guess a number: ")
