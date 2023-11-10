import time
currtime = time.time()

curr = 1

for divisor in range(2,21):
    if not (curr / divisor).is_integer():
        j = divisor
        k = 2
        temp = curr
        while(j > 1):
            if (j / k).is_integer():
                if not (temp / k).is_integer():
                    curr *= k
                else:
                    temp = temp / k
                j = j / k
                k = 1
            k += 1
            
print(curr)
print(time.time() - currtime)


