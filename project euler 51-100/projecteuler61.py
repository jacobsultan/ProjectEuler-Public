
tri = []
quad = []
quint = []
sex = []
sept = []
oct = []

for i in range(1000):
    tr = int((i * (i + 1)) / 2)
    qu = int( i ** 2)
    qui = int( ((i * (3 * i - 1)) / 2) )
    se = int((i * (2 * i - 1)))
    he = int(((i * ( 5 * i - 3)) / 2))
    oc = int(i * (3 * i - 2))
    if 10001> tr > 999:
        tri.append(tr)
    if 10001> qu> 999:
        quad.append(qu)
    if 10001>qui > 999:
        quint.append(qui)
    if 10001>se > 999:
        sex.append(se)
    if 10001>he > 999:
        sept.append(he)
    if 10001>oc > 999:
        oct.append(oc)

arr = []
arr.append(tri)
arr.append(quad)
arr.append(quint)
arr.append(sex)
arr.append(sept)
arr.append(oct)

tried = set()
finse = []
fin = []
newtried = set()
newfinse = []

def tryorders():

    if len(tried) == 6:
        print("done",finse)
        for num in finse:
            fin.append(num)
        return finse

    else:
        for i in range(6):
            if i not in tried:
                tried.add(i)
                for numbers in arr[i]:
                    if add(finse,numbers):
                        tryorders()
                        finse.pop()
                tried.remove(i)
            continue



    
               
            


def add(finset,numbers):
    if len(finset) == 0:
        finset.append(numbers)
        return True

    elif len(finset) == 5:
        if len(finset) == 5:
            if int(str(finset[-1])[2:]) == int((str(numbers))[:2]):
                if int(str(finset[0])[:2]) == int((str(numbers))[2:]):
                    finset.append(numbers)
                    print("Done",finset)
                    return True                 
    else:
        if int(str(finset[-1])[2:]) == int(str(numbers)[:2]):
            finset.append(numbers)
            return True

a = [8128, 2882, 8256, 5625, 2512, 1281]
print("sum",sum(a))

tryorders()   
print("fin",fin) 
print("finished")






            

