import time
timer = time.time()

maxfound = 1
k = 2
maxk = 600851475143 ** 0.5
targ = 600851475143


while k <= maxk:
    targholder = targ / k
    if targholder.is_integer():
        if k > maxfound:
            maxfound = k
        while((targholder / k).is_integer()):
            targholder /= k
        targ = targholder
        maxk = targholder ** 0.5
    k += 1

print(targholder)
print(time.time() - timer)

