import time
timenow = time.time()
primes = [2]
lastprime = 1
for i in range(2,10000):
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


def factors(whole):
    factors = []
    curr = whole
    for prime in primes:
        if curr == 1:
            break
        if prime > curr:
            break
        while (curr / prime).is_integer():
            factors.append(prime)
            curr = curr / prime
    return factors

for i in range(100):
    print("i",i,factors(i))