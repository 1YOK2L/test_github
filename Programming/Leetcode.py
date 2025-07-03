nums = input("Enter a set of numbers: ").split(", ")
TGT = input("Enter target number: ")

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

# Validate and convert TGT
if not isfloat(TGT):
    print("Your input is invalid.")
    exit()

TGT = float(TGT)
if abs(TGT) > 1e9:
    print("Number outside our bounds.")
    exit()

# Validate nums
if not (2 <= len(nums) <= 10**4):
    print("Your input is invalid.")
    exit()

my_list = []

for x in nums:
    if isfloat(x):
        num = float(x)
        if num.is_integer():
            num = int(num)
    else:
        print("Your input is invalid.")
        exit()
    
    if abs(num) > 1e9:
        print("Number outside our bounds.")
        exit()
    
    my_list.append(num)

# Search for a pair of indices
found = False
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if isinstance(TGT, float):
            if abs(my_list[i] + my_list[j] - TGT) <= 1e-9:
                print([i, j])
                found = True
                break
        else:
            if my_list[i] + my_list[j] == TGT:
                print([i, j])
                found = True
                break
    if found:
        break

if not found:
    print("No valid pair found.")
