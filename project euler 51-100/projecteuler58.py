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

print(time.time() - timenow)

def isprime(number):
    for num in primes:
        if num ** 2 > number:
            return True
        if (number / num).is_integer() and number != num:
            return False
    return True
            

numprimes = 3
totdiag = 4
sidelength = 3
curr = 9
while(numprimes/totdiag > 0.1):
    print("sidelength",sidelength,"curr",curr,"numprimes",numprimes,"totdiag",totdiag)
    sidelength += 2
    totdiag += 4
    for i in range(4):
        curr += sidelength - 1
        if isprime(curr):
            numprimes += 1
print(sidelength)