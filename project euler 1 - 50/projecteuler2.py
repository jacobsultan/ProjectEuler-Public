import time
start_time = time.time()
tot = 0
import time
holder = 0
curr = 1
prev = 1
while(curr < 400000000):
    holder = curr
    curr += prev
    prev = holder
    if curr % 2 == 0:
        tot += curr
print(tot)

print(time.time() - start_time)
