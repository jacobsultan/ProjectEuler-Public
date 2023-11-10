import time
currtime = time.time()

primecomp = {}
primes = []

for i in range(2,28124):
    curr = i
    comp = []
    seen = False
    for j in range(len(primes)):
        if primes[j] == curr:
            comp.append(curr)
            curr = 1
            break
        while (curr / primes[j]).is_integer():
            seen = True
            curr = curr / primes[j]
            comp.append(primes[j])
        if not seen:
            if primes[j] ** 2 > curr:
                break
    if curr > 1:
        comp.append(curr)
        primes.append(curr)
    primecomp[i] = comp

def mult(array,x,curr,use):
    if use:
        curr *= array[x]
    if x + 1 < len(array):
        mult(array,x+1,curr,True)
        mult(array,x+1,curr,False)
    else:
        properdivisors.add(curr)



dbset = set()
for item in primecomp.items():
    properdivisors = set()
    mult(item[1],0,1,True)
    mult(item[1],0,1,False)
    properdivisors.remove(item[0])
    summer = sum(properdivisors)
    if summer > item[0] and summer < 28123:
        dbset.add(item[0])


dbar = list(dbset)
dbar.sort()
tot = 1
for i in range(2,28123):
    curr = i
    notfound = True
    k = 0
    while(notfound):
        if curr - dbar[k] in dbset:
            notfound = False
        elif dbar[k] > curr:
            notfound = False
            tot += i
        elif k > 4112:
            notfound = False
            tot += i
        k += 1
print(tot)


print(time.time() - currtime)

        

        

    


