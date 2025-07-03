newlist = []
result = []
removed_character = "a"
newlist.append("cat")
newlist.append("dog")
newlist.append("rat")
newlist.append("bat")

for i in newlist:
    j = ""
    for k in i:
        if k != removed_character:
            j += k
    result.append(j)
print(result)