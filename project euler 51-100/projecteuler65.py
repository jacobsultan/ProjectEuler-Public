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

e = []
e.append(2)
e.append(1)
e.append(2)

k = 2

for i in range(98):
    if i % 3 == 0 or i % 3 == 1:
        e.append(1)
    else:
        e.append(k * 2)
        k += 1

def adder(top,bottom,next):
    nextpart = next * bottom
    newtop = nextpart + top
    return[bottom,newtop]

    return sharedfactors(newtop,bottom)


def sharedfactors(toppart,bottompart):
    print("sharedfactorsstart",toppart,bottompart)
    factors = []
    curr = toppart
    for prime in primes:
        if curr == 1:
            break
        while (curr / prime).is_integer():
            factors.append(prime)
            curr = curr / prime
    if curr > 1:
        factors.append(curr)
    i = 0
    print(factors)
    while i < len(factors):
        if (bottompart / factors[i]).is_integer():
            bottompart /= factors[i]
            factors.remove(factors[i])
        else:
            i += 1
    j = 1
    for factor in factors:
        j *= factor
    print("endsharedfactors",j,bottompart)
    return[int(bottompart),int(j)]


for i,nums in enumerate(e):
    print("i",i,"e",nums)

"""e= []
e.append(1)
e.append(2)
e.append(2)
e.append(2)
e.append(2)
e.append(2)
e.append(2)
e.append(2)
e.append(2)
e.append(2)
e.append(2)
e.append(2)
e.append(2)"""

jj = 99

curr = [1,e[jj]]
print("e{}".format(jj),e[jj])
print("curr",curr)



for i in range(jj - 1,0,-1):
    curr = adder(curr[0],curr[1],e[i])
    print("curr",i,curr)
curr[0] += e[0] * curr[1]
print("curr",0,curr)

tot = 0
for let in str(curr[0]):
    tot += int(let)
print("tot",tot)


"""2 yes, 3 yes, 4 no,5 yes, 6 yes, 7 no, 8 yes
tried 2,26,28,38,54
"""
