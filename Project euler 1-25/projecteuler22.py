import time
currtime = time.time()


f = open("C:/Users/jsult/Desktop/projecteuler/textfiles/0022_names.txt", "r")
line = f.readline()
c = line.split(",")
for i in range(len(c)):
    c[i] = c[i][1:-1]
c.sort()
tot = 0
for i in range(len(c)):
    name = c[i]
    nametot = 0
    for let in name:
        nametot += ord(let) - 64
    tot += nametot * (i + 1)

print(tot)

print(time.time() - currtime)
