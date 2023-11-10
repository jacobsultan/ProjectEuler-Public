import time
currtime = time.time()

arr = []

counter = 0
def round(curr,miss):
    if len(curr) == 10:
        test.append(curr)
    else:
        for i in range(10):
            if str(i) not in curr and i != miss:
                nex = curr + str(i)
                round(nex,miss)


test = []
test.append(round("2",2))


print(test[1000000 - (len(test)) * 2 +1])

print(time.time() - currtime)
