import time
start_time = time.time()

tot = 0
holder = 0
curr = 1
prev = 1

while(curr < 4 * 10 ** 6):
    holder = curr
    curr += prev
    prev = holder
    if curr % 2 == 0:
        tot += curr

print(tot)

print(time.time() - start_time)
