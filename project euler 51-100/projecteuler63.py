"""
not 43


1,4,9
16,25,36,49,64,81

2, 




"""



""" maybe tot + 1 if including 0 ^ 1"""
tot = 0
collection = []

for i in range(0,100):
    tot += len(collection)
    collection = []
    ndigit = i
    j = 9
    while(10 ** ndigit > j ** ndigit >= 10 ** (ndigit - 1)):
        collection.append(j)
        j -= 1

    print("ndigit",ndigit,"collection",collection)

print("tot",tot)

