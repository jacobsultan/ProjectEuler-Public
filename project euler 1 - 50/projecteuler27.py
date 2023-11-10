from operator import indexOf
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

setprimes = set(primes)
print(time.time() - timenow)
primes[0] = 1

def test(first,second,input):
    tot = input ** 2
    tot += first * input + second
    return tot

maxk = 1
reta = 1
retb = 1

for a in range(-1001,1001):
    for b in range(-1001,1001):
        producing = True
        k = 0
        while producing:
            result = test(a,b,k)
            if result not in setprimes:
                producing = False
            else:
                k += 1
        if k > maxk:
            maxk = k
            reta = a
            retb = b
print(time.time() - timenow)
print(maxk)
print(reta)
print(retb)