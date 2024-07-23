import time
timenow = time.time()
primes = [2]
lastprime = 1
for i in range(2,1000000):
    temp = i
    for prime in primes:
        if temp < lastprime:
            break
        elif prime ** 2 > i:
            if temp == i:
                primes.append(temp)
                lastprime = temp
            temp = 1
            break
        while (temp / prime).is_integer():
            temp = int(temp / prime)
            
"""primes[0] = 1"""
  
primeset = set(primes)

print(time.time() - timenow)

def sharedfactors(toppart,bottompart):
    print("sharedfactorsstart",toppart,bottompart)
    factors = []
    curr = toppart
    for prime in primes:
        if curr == 1:
            break
        if prime ** 2 > curr:
            break
        while (curr / prime).is_integer():
            factors.append(prime)
            curr = curr / prime
    """if prime is bigger than max prime ** 2, (next line)"""
    if curr > 1:
        factors.append(curr)
    i = 0
    print(factors)
    while i < len(factors):
        if (bottompart / factors[i]).is_integer():
            bottompart /= factors[i]
            factors.remove(factors[i])
        else:
            i += 1
    j = 1
    for factor in factors:
        j *= factor
    print("endsharedfactors",j,bottompart)
    return[int(bottompart),int(j)]