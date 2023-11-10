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
primeset = set(primes)

print(time.time() - timenow)

notfound = True
history = 0
i = 300

while(notfound):
    primeset = set()
    curr = i
    if i % 1000 == 0:
        print(i)

    for prime in primes:
        while (curr / prime).is_integer():
            curr = curr / prime
            primeset.add(prime)
        if curr == 1:
            break
    
   

    if len(primeset) == 4:
        history += 1
    else:
        history = 0

    if history == 4:
        print("done",i)
        notfound = False       

    i += 1

i - 3