IP1 = input("Input 1 : ")
IP2 = input("Input 2 : ")
IP3 = input("Input 3 : ")

if (IP1.isnumeric or (IP1[0] == "-" and IP1[1:-1].isnumeric)) and (IP2.isnumeric or (IP2[0] == "-" and IP2[1:-1].isnumeric)) and (IP3.isnumeric or (IP3[0] == "-" and IP3[1:-1].isnumeric)):
    x = int(IP1)
    y = int(IP2)
    z = int(IP3)
    print("Max Number is :", max(x, y, z))