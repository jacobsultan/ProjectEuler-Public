"""import time
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

def factorisation(number):
    counter = 0
    arr = []
    while(number > 1 and primes[counter] **2 < number):
        test = primes[counter]
        while(number / test).is_integer():
            number = int(number / test)
            arr.append(test)
        counter += 1
    if number > 1:
        arr.append(number)
    return arr"""


"""def cancelled(arrtop,arrbottom):
    i = 0
    while(i < len(arrtop)):
        curr = arrtop[i]

        if curr in arrbottom:
            print("HERE")
            arrtop.remove(curr)
            arrbottom.remove(curr)
        else:
            i += 1
    mult1 = 1
    mult2 = 1
    for num in arrtop:
        mult1 *= num
    for num in arrbottom:
        mult2 *= num
    return [mult1,mult2]
        

"""
top = 3
bottom = 2
counter = 0
for i in range(2,1001):
    print("")
    print("i",i,"top",top,"bottom",bottom)
    hold = top
    top += 2 * bottom
    bottom += hold
    """pair = cancelled(factorisation(top),factorisation(bottom))
    top = pair[0]
    bottom = pair[1]"""
    if len(str(top)) > len(str(bottom)):
        print("here")
        counter += 1
print(counter)
