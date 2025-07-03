x = input("Input a number: ")
if x.isnumeric() or (x[0] == "-" and x[1:].isnumeric()):
    x = int(x)
    if x % 2 == 0:
        print(f'Number "{x}" is even')
    else:
        print(f'Number "{x}" is odd')
else:
    print("Invalid input")
