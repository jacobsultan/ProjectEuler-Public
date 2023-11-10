primes = [2]
for i in range(2,10000):
    temp = i
    for prime in primes:
        if prime ** 2 > i:
            if temp == i:
                primes.append(temp)
                lastprime = temp
            temp = 1
            break
        while (temp / prime).is_integer():
            temp = int(temp / prime)  

print(primes)
print(len(primes))
print("")





for i in range(len(primes)):
    
    
    first = primes[i]
    if first < 1000:
        continue
    stringfirst = str(first)
    firstset = set()
    for let in stringfirst:
        firstset.add(let)
    for j in range(i + 1,len(primes)):
        good = True
        second = primes[j]
        stringsecond = str(second)
        for let in stringsecond:
            if let not in firstset:
                good = False
        if good:    
            for k in range(j + 1,len(primes)):
                good = True
                third = primes[k]
                stringthird = str(third)
                for let in stringthird:
                    if let not in firstset:
                        good = False
                
                if good:
                    if second - first == third - second:
                        print("DONE",first,second,third)
                        break