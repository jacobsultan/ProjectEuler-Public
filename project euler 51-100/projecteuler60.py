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


def isprime(number):
    for i in range(len(primes)):
        if primes[i] ** 2 > number:
            return True
        elif (number / primes[i]).is_integer():
            return False

def test(number,group):
    string = str(number)
    for num in group:
        if int(string + str(num)) not in primeset:
            if not isprime(int(string + str(num))):
                return False
        if int(str(num) + string) not in primeset:
            if not isprime(int(str(num) + string)):
                return False
    return True
"""
a = set()
a.add(3)
a.add(7)
a.add(109)
print(test(673,a))


"""
fingroup = set()
notfound = True
first = 1
tot = 10000000000000
while(first < len(primes)):

    firstprime = primes[first]
    if firstprime > tot / 4:
        print("first prime too big",firstprime)
        break
    print("first",first,"firstprime",firstprime)

    primegroup = set()
    primegroup.add(firstprime)
    for secondind in range(first + 1,len(primes)):
        secondprime = primes[secondind]
        if test(secondprime,primegroup):
            primegroup.add(secondprime)
            for thirdind in range(secondind + 1, len(primes)):
                thirdprime = primes[thirdind]
                if test(thirdprime,primegroup):
                    primegroup.add(thirdprime)
                    for fourthind in range(thirdind + 1,len(primes)):
                        fourthprime = primes[fourthind]
                        if test(fourthprime,primegroup):
                            primegroup.add(fourthprime)
                            for fifthind in range(fourthind + 1, len(primes)):
                                fifthprime = primes[fifthind]
                                if test(fifthprime,primegroup):
                                    notfound = False
                                    primegroup.add(fifthprime)
                                    print(primegroup)
                                    print("")
                                    print("DONE")
                                    print("")
                                    if sum(primegroup) < tot:
                                        total = sum(primegroup)
                                        fingroup = set()
                                        for zz in primegroup:
                                            fingroup.add(zz)

                        if notfound and len(primegroup) == 4:
                            primegroup.remove(fourthprime)
                if notfound and len(primegroup) == 3:

                    primegroup.remove(thirdprime)
        if notfound and len(primegroup) == 2:
            primegroup.remove(secondprime)


    first += 1


print("tot",tot)
print("fingroup",fingroup)
