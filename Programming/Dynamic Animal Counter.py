mydict = {}

while (x := input("Enter an animal or 'q' to quit: ").strip().lower()) != 'q':
    if x:
        mydict[x] = mydict.get(x, 0) + 1 
print()
for animal, count in mydict.items():
    print(f"{animal} : {count}")