mapping = {}
mapping[0] = 1
mapping[1] = 1
for i in range(2,10):
    curr = 1
    for j in range(1,i + 1):
        curr *= j
    mapping[i] = curr

print(mapping)


fin = []
for i in range(10000000):
    if i % 10000 == 0:
        print(i)
    curr = i
    string = str(curr)
    if "8" in string:
        if curr < 40000:
            continue
    if "9" in string:
        if curr <350000:
            continue
    if i > 110000:
        if string.count("9") < 2:
            continue
    elif i > 350000:
        if "9" not in string:
            continue
    tot = 0
    for let in string:
        tot += mapping[int(let)]
    if tot == i:
        fin.append(i)
print(fin)

    


