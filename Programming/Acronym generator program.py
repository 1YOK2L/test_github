def acronym(string):
    string = input()
    x = string.split()
    for i in range(len(x)):
        a = (x[i][0]).upper()
        print(a, end = "")
    print()
acronym("")
acronym("")