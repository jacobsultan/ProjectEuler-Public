

def fact(n,r):
    val = 1
    bottomleft = 1
    bottomright = 1
    top = 1
    while (top <= n or bottomleft <= r and bottomright <= n - r) or (bottomleft == r and bottomright == n - r and val > 1000000):
        
        if bottomleft <= r:
            val /= bottomleft
        if bottomright <= n-r:
            val /= bottomright
        if top <= n:
            val *= top

        bottomleft += 1
        bottomright += 1
        top += 1


    print("top",top,"bottomleft",bottomleft,"bottomright",bottomright,"val",val)
    print("n",n,"r",r,"val",val)
    return val > 1000000
print(fact(55,0))


counter = 0
for n in range(101):
    print("n",n)
    for r in range(n + 1):
        if fact(n,r):
            counter += 1

print(counter)

    
    