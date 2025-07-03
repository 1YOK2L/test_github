nums = input("Enter a string: ").split(", ")
TGT = input("Enter target number: ")
my_list = []
result = []
def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if isfloat(TGT):
    TGT = float(TGT)
    if TGT >= -10 ** 9 and TGT <= 10 ** 9:
        if len(nums) >= 2 and len(nums) < 10 ** 4:
            for x in nums:
                if isfloat(x) and not isint(x):
                    x = float(x)
                elif x.isnumeric() or (x[0] == "-" and x[1:].isnumeric()):
                    x = int(x)
                my_list.append(x)
                if x < -10 ** 9 or x > 10 ** 9:
                    print("Number outside our bounds.")
                    break
            if isint(TGT):
                TGT = int(TGT)
            elif isfloat(TGT):
                TGT = float(TGT)
            for i in range(len(my_list)):
                for j in range(len(my_list)):
                    if i == j:
                        continue
                    else:
                        n = my_list[i] + my_list[j]
                        if n == TGT:
                            result.append(i)
                            result.append(j)
                            print(sorted(result))
                            break
                    break
        else:
            print("Your input is invalid.")
    else:
        print("Number outside our bounds.")
else:
    print("Your input is invalid.")