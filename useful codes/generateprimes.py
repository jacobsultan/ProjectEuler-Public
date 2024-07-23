primes = [2]
i = 3
while i < 2000000:
    if i % 10000 == 0:
        print(i)
    temp = i
    for prime in primes:
        if temp < primes[-1]:
            break
        elif prime ** 2 > i:
            break
        while (temp / prime).is_integer():
            temp = int(temp / prime)
    if temp == i:
        primes.append(i)
    i += 1