import time
currtime = time.time()

maxfound = 0
for i in range(999,99, - 1):
    for j in range(999,99,-1):
        curr = i * j
        if curr > maxfound:
            backwards = str(curr)[::-1]
            if str(curr) == backwards:
                maxfound = curr

print(maxfound)
print(time.time() - currtime)
