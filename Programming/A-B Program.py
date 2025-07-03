num = int(input("Enter a number: "))
x = int(num)

if x % 3 == 0 and x % 5 != 0:
    print("A")
elif x % 5 == 0 and x % 3 != 0:
    print("B")
elif x % 15 == 0:
    print("AB")
else:
    print(num)