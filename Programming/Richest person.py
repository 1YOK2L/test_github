my_list = []
while (name := input("Please enter name 'q' to quit: ")) != "'q'":
    salary = float(input("Please enter salary : "))
    a = {"name":name, "salary":salary}
    my_list.append(a)

newlist = sorted(my_list, key = lambda d: d['salary'], reverse = True)
for i in newlist:
    print(f"{i["name"]} with salary", i["salary"])