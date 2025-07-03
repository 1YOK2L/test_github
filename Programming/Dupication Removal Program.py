new_list = list()
new_list.append(1)
new_list.append(2)
new_list.append(3)
new_list.append(4)
new_list.append(5)
new_list.append(5)
new_list.append(4)
new_list.append(3)
new_list.append(2)
new_list.append(1)
print(new_list)
new_list_result = []
for i in new_list:
    if i in new_list_result:
        del(i)
    else:
        new_list_result.append(i)
print(new_list_result)