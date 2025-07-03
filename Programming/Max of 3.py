curr_max = int(input("Input 1 : "))
curr_max = input_2 if curr_max < (input_2 := int(input("Input 2 : "))) else curr_max
curr_max = input_3 if curr_max < (input_3 := int(input("Input 3 : "))) else curr_max
print(f"Max number is : {curr_max}")