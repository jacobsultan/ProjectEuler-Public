import time

timenow = time.time()
primes = [2]
lastprime = 1
for i in range(2,33000):
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

"""
print(time.time() - timenow)
print(len(primes))
notfound = True
i = 1229
while notfound:
    curr = primes[i]    
    print(curr)

    strcurr = str(curr)
    setcurr = set()
    

    for let in strcurr:
        setcurr.add(let)

    if "9" in setcurr or "8" in setcurr or "7" in setcurr or "0" in setcurr or "6" in setcurr or "5" in setcurr:
        i -= 1
        continue

    if len(setcurr) == 4:
        print("strcurr",strcurr)
        notfound = False
        break
    i -= 1


print("i",i)
print("primes",primes[i])
"""
"""
print("primes",primes)
eipan = []
def place(string):
    if len(string) == 8:
        eipan.append(string)
    else:
        for i in range(1,9):
            if str(i) not in string:
                place(string + str(i))
place("")
eipan.sort()
print(len(eipan))

k = 40319
notfound = True


while(notfound):
    curr = int(eipan[k])
    print("curr",curr)
    while(curr > 1):
        for prime in primes:

            while (curr / prime).is_integer():
                curr = curr / prime
            if curr == 1:
                break
        if curr == eipan[k]:
            notfound = False
            print("done",curr)
            curr = 1
        break
    k -= 1





print("k",k,"eipan[k]",eipan[k])

"""

eipan = []

def place(string,top):
    if len(string) == top:
        eipan.append(string)
    else:
        for i in range(1,top + 1):
            if str(i) not in string:
                place(string + str(i),top)


for i in range(1,10):
    place("",i)

print("len",len(eipan))

k = 409112
notfound = True

while(notfound and k > 0):
    curr = int(eipan[k])
    if k % 1000 == 0:
        print(k)
    while(curr > 1):
        for prime in primes:
            while (curr / prime).is_integer():
                if curr == prime == int(eipan[k]):
                    print(prime)
                curr = curr / prime
                
                break

            if curr < 1000:
                break

        if curr == int(eipan[k]):
            notfound = False
            print("done",curr)
            curr = 1
        break
    k -= 1

print(eipan[k])





print("k",k,"eipan[k]",eipan[k])



