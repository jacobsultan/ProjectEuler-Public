
tot = 0

import time
timenow = time.time()
prifac = {}
for i in range(1,1001):
    prifac[i] = []

prifac[1].append(1)
prifac[2].append(2)

primes = [2]
for i in range(3,1001):
    temp = i
    for prime in primes:
        if prime ** 2 > i:
            if temp == i:
                primes.append(temp)
                prifac[i] = [temp]
            else:
                prifac[i].append(temp)
            break
        while (temp / prime).is_integer():
            temp = int(temp / prime)
            prifac[i].append(prime)

print("")
totfac = {}
for key,value in prifac.items():

    for nums in value:
        if nums in totfac:
            totfac[nums] += key
        else:
            totfac[nums] = key
totfac[1] = 1

print(prifac)

tot = 0
for key,value in prifac.items():
    curr = 1
    print("key",key)
    
    for i in range(key):
        for nums in value:
            curr = curr * nums

            if curr > 100000000000:
                curr = curr % 100000000000
    tot += curr

    print("tot",tot)
    """5989245360"""