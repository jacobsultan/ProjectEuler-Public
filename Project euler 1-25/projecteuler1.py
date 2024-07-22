

import time
start_time = time.time()
tot = 0
for i in range(3,1000,3):
    tot += i
for i in range(5,1000,5):
    tot += i
for i in range(15,1000,15):
    tot -= i
print(tot)
print("Process finished --- %s seconds ---" % (time.time() - start_time))

