import time
currtime = time.time()

start = 1
mapping = {}
maxlen = 0
maxstart = 0

while(start <= 1000000):
    thislen = 1
    currchain = []
    curr = start
    currchain.append(curr)

    while(curr != 1):
        if curr in mapping:
            thislen += mapping[curr] - 1
            break
        elif curr % 2 == 0:
            curr = curr / 2
            thislen += 1
            currchain.append(curr)
        else:
            curr = curr * 3 + 1
            thislen += 1
            currchain.append(curr)
            
    for i in range(1,len(currchain) + 1):
        mapping[currchain[-i]] = thislen - len(currchain) + i 

    if thislen > maxlen:
        maxlen = thislen
        maxstart = start

        
    start += 1

print(maxstart)
print(time.time() - currtime)


