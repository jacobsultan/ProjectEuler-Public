import time
timenow = time.time()

primes = []
curr = 1
max = 1
while(max < 2000000):
    temp = curr
    while(temp > max):
        for prime in primes:
            if prime ** 2 > temp:
                break
            elif temp < max:
                break
            elif (temp / prime).is_integer():
                temp = temp / prime
                break
        if temp == curr:
            primes.append(temp)   
            max = temp
            break
    curr += 1


print(sum(primes) - max)
print(time.time() - timenow)

