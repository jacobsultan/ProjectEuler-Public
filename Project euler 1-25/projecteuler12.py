import time
timenow = time.time()

tri = 1
nex = 2

factors = set()
primes = []
primes.append(2)
tot = 0

while(tot <500):
    curr = tri
    factors = {}
    while(curr > 1):
        for prime in primes:
            if prime == curr:
                factors[prime] = 1
                curr = 1
                break
            elif prime > curr:
                break
            while (curr / prime).is_integer():
                curr /= prime
                if prime in factors:
                    factors[prime] += 1
                else:
                    factors[prime] = 1
        if curr > 1:
            primes.append(curr)
            curr = 1  
            break
    tot = 1
    for value in factors.values():
        tot *= value + 1
    tri += nex
    nex += 1

print("done",tri - nex + 1)
print(time.time()-timenow)
