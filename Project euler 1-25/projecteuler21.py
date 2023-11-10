import time
currtime = time.time()

primecomp = {}
primes = []

for i in range(2,10000):
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



db = {}

for item in primecomp.items():
    properdivisors = set()
    mult(item[1],0,1,True)
    mult(item[1],0,1,False)
    properdivisors.remove(item[0])
    db[item[0]] = sum(properdivisors)

tot = 0

for i in range(2,10000):
    k = db[i]
    if k > i and k < 10000:
        if db[k] == i:
            tot += i
            tot += k

print(tot)

print(time.time() - currtime)


  
        

        

    


