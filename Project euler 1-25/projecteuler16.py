import time
currtime = time.time()

a = str(2** 1000)
tot = 0
for let in a:
    tot += int(let)
print(tot)

print(time.time() - currtime)


