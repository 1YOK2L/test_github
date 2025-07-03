def acronym(string):
    string = str(string)
    x = string.split()
    for i in range(len(x)):
        a = (x[i][0]).upper()
        print(a, end = "")
    print()
acronym("Portable network graphics")
acronym("Information technology")
