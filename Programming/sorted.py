given_list = [17, 5, 12, 3, 45, 13, 32, 9, 4, 49, 29, 24]

def sortedlist(x):
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                a = x[j]
                x[j] = x[j+1]
                x[j+1] = a
                #a -> x[j] -> x[j+1] -> a
    print(x)

sortedlist(given_list)