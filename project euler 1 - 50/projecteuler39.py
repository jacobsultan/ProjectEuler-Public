squares = {}
for i in range(1000):
    squares[i]  = i ** 2

pmax = 3
pind = 120
pcount = {}
for p in range(1000):
    print("")
    print("p",p)
    pcombo = 0

    for c in range(int(p / 3),p):
        for a in range(p - c):

            if a >= c:
                break

            elif p-c-a > a:
                continue

            else:
                b = p - c - a
                if squares[a] + squares[b] == squares[c]:
                    print("foundone", "a",a,"b",b,"c",c)
                    pcombo += 1
    if pcombo > pmax:
        pmax = pcombo
        pind = p

    pcount[p] = pcombo

print(pind,pcount)
print("pcount", pcount) 




