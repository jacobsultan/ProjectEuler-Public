import time
currtime = time.time()


tot = 1
for i in range(1,101):
    tot *= i
st = str(tot)
fin = 0
for i in range(len(st)):
    fin += int(st[i])
print(fin)

print(time.time() - currtime)
