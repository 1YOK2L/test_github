Square = []
while (x := input("Input > ")) != 'q':
    def isfloat(s):
        try:
            float(s)
            return(True)
        except ValueError:
            return(False)
    def isint(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    if isfloat(x) and not isint(x):
        x = float(x)
    elif x.isnumeric or (x[0] == "-" and x[1:].isnumeric):
        x = int(x)
    y = x ** 2
    Square.append(y)
print(Square)
