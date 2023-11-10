import time
timenow = time.time()

primes = set()
curr = 1
while(len(primes) < 10001):
    temp = curr
    while(temp > 1):
        for prime in primes:
            if (temp / prime).is_integer():
                temp = temp / prime
                break
        if len(primes) == 10001:
            print("DONE",temp)
        if temp == curr:
            primes.add(temp)
            break
    curr += 1
    
if len(primes) == 10000:
    print(temp)


print(time.time() - timenow)

