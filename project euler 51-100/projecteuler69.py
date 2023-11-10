
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


def factors(whole):
    factors = []
    curr = whole
    for prime in primes:
        if curr == 1:
            break
        if prime ** 2 > curr:
            break
        while (curr / prime).is_integer():
            if prime not in factors:
                factors.append(prime)
            curr = curr / prime
    if curr > 1:
        factors.append(curr)
    return factors

primesfactors = {}

for i in range(2,1000000):
    if i % 1000 == 0:
        print("i",i)
    primesfactors[i] = factors(i)

maxratio = 0
maxnum = 0

currarr = []
max = []


choices = {}

def choose(poss,ask,curr):
    if len(curr) == ask:
        choices[poss][ask - 1].append(curr)
    else:
        if len(curr) == 0:
            for i in range(0,poss):
                curr += str(i)
                choose(poss,ask,curr)
                curr = ""
        else:
            for i in range(int(curr[-1]) + 1, poss):
                curr += str(i)
                choose(poss,ask,curr)
                curr = curr[:len(curr) - 1]



for i in range(1,8):
    bigger = []
    for j in range(0,i):
        now = []
        bigger.append(now)
    choices[i] = bigger


for i in range(1,8):
    for j in range(1,i + 1):
        choose(i,j,"")
   
print(choices)





def trycombos(ognum,choosenum,factor):
    inthere = []
    variations = choices[len(factor)][choosenum -1]
    for var in variations:
        tot = 1
        for num in var:
            tot *= factor[int(num)]
        inthere.append(int((ognum - 1) / tot))
    return inthere







def phi(number):
    tot = number
    factor = primesfactors[number]
    if len(factor) == 1 and factor[0] == number:
        
        return number - 1

    for j in range(1,len(factor) + 1):
        fins = trycombos(number,j,factor)

        if j % 2 == 0:
            for numberr in fins:
                tot += (numberr )
        else:
            for numberr in fins:
                tot -= numberr 
        
    return tot - 1


for i in range(3,1000000):
    phival = phi(i)
    if i / phival > maxratio:
        maxratio = i / phival
        maxnum = i

print("maxratio",maxratio,"maxnum",maxnum)
print("done")
