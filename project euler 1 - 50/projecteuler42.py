f = open("p042_words.txt", "r")
line = f.readline()
c = line.split(",")
for i in range(len(c)):
    c[i] = c[i][1:-1]



fin = 0
triangleset = set()
maxtri = 0
for i in range(10000):
    k = 0.5 * i * (i + 1)
    triangleset.add(k)
    if i == 9999:
        maxtri = k

print(triangleset)


for i in range(len(c)):
    tot = 0
    for let in c[i]:
        tot += ord(str.lower(let)) - 96
    print(tot)
    if tot in triangleset:
        fin += 1
    elif tot > maxtri:
        print("MAX")
print("done",fin)