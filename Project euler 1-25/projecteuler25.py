import time
currtime = time.time()

fib = {}
fib[1] = 1
fib[2] = 1
n = 3
curr = ""
while(len(curr) < 1000):
    fib[n] = fib[n- 1] + fib[n - 2]
    curr = str(fib[n])
    n += 1
print(n-1)

print(time.time() - currtime)
