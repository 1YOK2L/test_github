mydict = {"cat": 0, "bat": 0, "rat": 0, "dog": 0}
while (x := input(f"cat, bat, rat, dog, or \'q\' to quit : ").lower()) != 'q':
    if x in "cat":
        mydict["cat"] += 1
    elif x in "bat":
        mydict["bat"] += 1
    elif x in "rat":
        mydict["rat"] += 1
    elif x in "dog":
        mydict["dog"] += 1
print(f"\ncat : {mydict["cat"]}\nbat : {mydict["bat"]}\nrat : {mydict["rat"]}\ndog : {mydict["dog"]}")