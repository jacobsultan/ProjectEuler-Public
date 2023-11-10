

pents = []
for i in range(1,50000000):
    pent = int((i * ((3 * i) - 1 )) / 2)
    pents.append(pent)
pentset = set(pents)

mind = 1000000000
mini = 0
minj = 0
print(len(pents))

print(pents[1020])
print(pents[2167])

print(pents[1021])
print(pents[2168])

for i in range(0,50000000):
    if i % 100000 == 0:
        print("i",i)
    for j in range(i,50000000):
        if pents[j] - pents[i] > 5582660:
            break
        if int(pents[i] + pents[j]) in pentset:
            if int(pents[j] - pents[i]) in pentset:
                print("i",i,"j",j)
                if pents[j] - pents[i] < mind:
                    mind = pents[j] - pents[i]
                    mini = i + 1
                    minj = j + 1
print(mind)
print(mini)
print(minj)