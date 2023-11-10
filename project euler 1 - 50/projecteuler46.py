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

squares = []
for i in range(100000):
    squares.append(i ** 2)



for i in range(33,1000000,2):
    if i in primeset:
        continue
    for square in squares:
        if (i - 2 * square) in primeset:
            break
        elif 2 * square > i:
            print("found",i)

    
