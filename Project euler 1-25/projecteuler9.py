import time
newtime = time.time()

done = False

for c in range(1000,0,-1):
    ab = 1000 - c
    if c ** 2 > ab ** 2:
        continue
    for a in range(ab-1,int(ab / 2), -1):
        b = ab - a
        if c ** 2 == a ** 2 + b ** 2:
            print("a",a)
            print("b",b)
            print("c",c)
            done = True
        if done:
            break
    if done:
        break

print(a * b * c )
print(time.time() - newtime)
