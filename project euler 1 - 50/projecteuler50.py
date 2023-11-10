import time
timenow = time.time()
primes = [2]
lastprime = 1
for i in range(2,100000):
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
primeset = set(primes)
primes[0] = 1

maximum = 8
bigprimes = 0
bigi = 1

for consec in range(8, 550):
    print(consec)
    for i in range(78499 - consec):
        tot = sum(primes[i:i + consec])
        if tot > 1000000:
            break
        elif tot in primeset:
            maximum = consec
            bigi = i
            bigprime = tot

print(bigi)
print(maximum)
print(bigprimes)


print(sum(primes[4:547]))
