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
ret = []
for prime in primes:
    madeit = True
    curr = prime
    string = str(curr)
    for i in range(1,len(string)):
        string = string[1:]
        if int(string) not in primeset:
            madeit = False
            break

    if madeit:
        if curr > 10:
            ret.append(curr)

print(len(ret))
fin = []
for att in ret:
    attst = str(att)[:-1]
    if int(attst) in primeset:
        madeit = True
        for i in range(1,len(attst)):
            attst = attst[:-1]
            if int(attst) not in primeset:
                madeit = False
                break
        if madeit:
            if curr > 10:
                fin.append(att)

print("fin",fin)
print("HERE", len(fin))


print(sum(fin))    
