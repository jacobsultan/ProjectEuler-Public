"""4,1,4  3,2,4 """

finset = set()
aset = []
bset = []
cset = []

for first in range(1,10):
    print("first",first)
    a = first * 1000
    for second in range(1,10):
        print("second",second)
        a += second * 100 
        for third in range(1,10):
            a += third * 10
            for fourth in range(1,10):
                a += fourth
                for fifth in range(1,10):
                    b = fifth
                    c = a * b
                    cstring = str(c)
                    astring = str(a)
                    bstring = str(b)
                    cser = set()

                    for let in cstring:
                        cser.add(let)
                    for let in bstring:
                        cser.add(let)
                    for let in astring:
                        cser.add(let)
                    if len(cstring) == 4 and len(cser) == 9 and "0" not in cser:
                        aset.append(a)
                        bset.append(b)
                        cset.append(c)



                a -= fourth
            a -= third * 10
        a -= second * 100

for i in range(len(aset)):
    print(aset[i],bset[i],cset[i])
    finset.add(cset[i])


aset = []
bset = []
cset = []

for first in range(1,10):
    print("first",first)
    a = first * 100
    for second in range(1,10):
        print("second",second)
        a += second * 10
        for third in range(1,10):
            a += third
            for fourth in range(1,10):
                b = fourth * 10
                for fifth in range(1,10):
                    b += fifth
                    c = a * b
                    cstring = str(c)
                    astring = str(a)
                    bstring = str(b)
                    cser = set()

                    for let in cstring:
                        cser.add(let)
                    for let in bstring:
                        cser.add(let)
                    for let in astring:
                        cser.add(let)
                    if len(cstring) == 4 and len(cser) == 9 and "0" not in cser:
                        aset.append(a)
                        bset.append(b)
                        cset.append(c)
                    b -= fifth
                b -= fourth * 10
            a -= third
        a -= second * 10

for i in range(len(aset)):
    print(aset[i],bset[i],cset[i])
    finset.add(cset[i])
print(finset)
print(sum(finset))





