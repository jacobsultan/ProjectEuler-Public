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

print(time.time() - timenow)
print(primes)
primeset = set(primes)
ret = []

for i in range(1000000):
    if i % 10000 == 0:
        print(i  / 10000)
    if i in primeset:
        rotationsprime = True
        string = str(i)
        for nex in range(1,len(string)):
            string = string[1:] + string[0]
            curr = int(string)
            if curr not in primeset:
                rotationsprime = False
                break
        if rotationsprime:
            ret.append(i)

print(len(ret))
