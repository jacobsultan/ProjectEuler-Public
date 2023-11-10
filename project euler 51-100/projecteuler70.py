zz = 1000000
import time
timenow = time.time()
primes = [2]
lastprime = 1
for i in range(2,32000):
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



for i in range(2,zz * 10):
    if i % 100000 == 0:
        print("i",i)
    primesfactors[i] = factors(i)

minratio = 100
minnum = 0

currarr = []
max = []

maxie = 0
for num in primesfactors:
    if len(primesfactors[num]) > maxie:
        maxie = len(primesfactors[num])
        print("maxie",maxie)


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



for i in range(1,9):
    bigger = []
    for j in range(0,i):
        now = []
        bigger.append(now)
    choices[i] = bigger


for i in range(1,9):
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


def isperm(num1,num2):
    str1 = str(num1)
    str2 = str(num2)
    if len(str1) != len(str2):
        return False
    ark = []
    for let in str1:
        ark.append(let)
    for let in str2:
        if let not in ark:
            return False
        ark.remove(let)
    return len(ark) == 0

minratio = 10
minval = 1

for i in range(3,zz * 10):

    if i % 10000 == 0:
        print("i",i)
    phival = phi(i)

    if 1000000 >i > 999990:
        print("i",i,"phival",phival)
    if i == 87109:
        print("here",phival)
    
    if isperm(i,phival):
        if i / phival < minratio:
            minratio = i /phival
            minnum = i
            print("")
            print("ratio",i / phival)
            print("i",i,"phival",phival)
       

print("donehere")
print("max",maxie)
