import time
currtime = time.time()

tot1 = 0
add = 0
for i in range(1,101):
    add += i
    tot1 += i * i

print(add * add - tot1)
print(time.time() - currtime)
