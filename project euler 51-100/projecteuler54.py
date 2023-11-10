f = open("p054_poker.txt", "r")

def ranktoname(num):
    if num == 1:
        return "high card"
    elif num == 2:
        return "pair"
    elif num == 3:
        return "twopair"
    elif num == 4:
        return "three of a kind"
    elif num == 5:
        return "straight"
    elif num == 6:
        return "Flush"
    elif num == 7:
        return "full house"
    elif num == 8:
        return "4 of a kind"
    elif num == 9:
        return "straight flush"
    elif num == 10:
        return "Royal flush"





def tonum(let):

    if let == "J":
        return 11
    elif let == "Q":
        return 12
    elif let == "K":
        return 13
    elif let == "A":
        return 14
    elif let == "T":
        return 10
    else:
        return int(let)


def ranking(p):
    
        
    pnum = []
    psuit = []
    
    for i in range(5):
        pnum.append(p[i][0])
        psuit.append(p[i][1])
    
    for i in range(5):
        pnum[i] = tonum(pnum[i])
    

    psuitset = set(psuit)
    pnumset = set(pnum)
    if len(psuitset) == 1:
        if 14 in pnum:
            if 13 in pnum:
                if 12 in pnum:
                    if 11 in pnum:
                        if 10 in pnum:
                            return 10 
                            """royalflush"""
        min = 15
        max = 0
        for num in pnum:
            if num < min:
                min = num
            if num > max:
                max = num
        if len(pnumset) == 5:
            if min == max - 4:
                return 9
                """straightflush"""
    if len(pnumset) == 2:
        a = pnumset.pop()
        acount = 0
        for num in pnum:
            if num == a:
                acount += 1
        if acount == 1 or 4:
            return 8
            """four of a kind"""
        else:
            return 7
            """fullhouse"""
    if len(psuitset) == 1:
        return 6
        """flush"""
    min = 15
    max = 0
    for num in pnum:
        if num < min:
            min = num
        if num > max:
            max = num

    if len(pnumset) == 5:
        if min == max - 4:
            return 5
            """straight"""

    if len(pnumset) == 3:
        a = pnumset.pop()
        b = pnumset.pop()
        acount = 0
        bcount = 0
        for num in pnum:
            if num == a:
                acount += 1
            if num == b:
                bcount += 1
        if acount == 3 or bcount == 3 or (acount == 1 and bcount == 1):
            return 4
            """three of a king"""
        else:
            return 3
            """two pairs"""
    if len(pnumset) == 4:
        return 2
        """onepair"""
    return 1
    """highcard"""
    
def highercards(p1,p2):


    if max(p1) > max(p2):
        return True
    elif max(p1) < max(p2):
        return False
    else:
        max1 = max(p1)
        max2 = max(p2)
        notfound = True
        while(notfound):
            nex1 = 0
            nex2 = 0
            for num in p1:
                if num > nex1 and num < max1:
                    nex1 = num
            for num in p2:
                if num > nex2 and num < max2:
                    nex2 = num
            if nex1 > nex2:
                return True
            if nex2 > nex1:
                return False
            max1 = nex1
            max2 = nex2

def findpair(p):
    pset = set(p)
    pcop = []
    for num in p:
        pcop.append(num)


    for i in range(len(pset)):
        pcop.remove(pset.pop())
    return pcop.pop()

def highertwopairs(p):
  
    pset = set(p)
    a = pset[0]
    b = pset[1]
    acount = 0
    bcount = 0
    for num in p:
        if num == a:
            acount += 1
        elif num == b:
            bcount += 1
    if acount == 2 and bcount == 2:
        return max(a,b)
    elif acount == 2:
        return max(a,pset[2])
    else:
        return max(b,pset[2])

def downtopairs(p1,p2):
    p1pair = findpair(p1)
    p2pair = findpair(p2)

    if p1pair > p2pair:
        return True
    elif p1pair < p2pair:
        return False
    else:
        p1.remove(p1pair)
        p1.remove(p1pair)
        p2.remove(p2pair)
        p2.remove(p2pair)
        return highercards(p1,p2)

def find3(p):

    pset = set(p)
    a = pset[0]
    b = pset[1]
    acount = 0
    bcount = 0
    for num in p:
        if num == a:
            acount += 1
        elif num == b:
            bcount += 1
    if acount == 3:
        return pset[0]
    elif bcount == 3:
        return pset[1]
    else:
        return pset[2]
   
    


def p1better(p1,p2,ranking):
    
    if ranking == 1:
       
        return highercards(p1,p2)
    elif ranking == 2:
        return downtopairs(p1,p2)
    elif ranking == 3:

        p1pair = highertwopairs(p1)
        p2pair = highertwopairs(p2)

        if p1pair > p2pair:
            return True
        elif p1pair < p2pair:
            return False
        else:
            p1.remove(p1pair)
            p1.remove(p1pair)
            p2.remove(p2pair)
            p2.remove(p2pair)
            return downtopairs(p1,p2)
    elif ranking == 4:
        p13 = find3(p1)
        p23 = find3(p2)
        if p13 > p23:
            return True
        elif p23 > p13:
            return False
        else:
            p1.remove(p13)
            p1.remove(p13)
            p1.remove(p13)
            p2.remove(p23)
            p2.remove(p23)
            p2.remove(p23)
        return highercards(p1,p2)


    elif ranking == 5 or ranking == 6 or ranking == 9:     
        return max(p1,p2) == max(p1)
    elif ranking == 7:
        p13 = find3(p1)
        p23 = find3(p2)
        if p13 > p23:
            return True
        elif p23 > p13:
            return False
        else:
            p1.remove(p13)
            p1.remove(p13)
            p1.remove(p13)
            p2.remove(p23)
            p2.remove(p23)
            p2.remove(p23)
            return downtopairs(p1,p2)
    elif ranking == 8:
        if p1[0] == p1[1]:
            p14 = p1[0]
        else:
            if p1[2] == p1[1]:
                p14 = p1[1]
            else:
                p14[0]

        if p2[0] == p2[1]:
            p24 = p2[0]
        else:
            if p2[2] == p2[1]:
                p24 = p2[1]
            else:
                p24[0]
        p13 = find3(p1)
        p23 = find3(p2)

        if p14 > p24:
            return True
        elif p24 > p14:
            return False
        else:
            p1.remove(p14)
            p1.remove(p14)
            p1.remove(p14)
            p1.remove(p14)
            p2.remove(p24)
            p2.remove(p24)
            p2.remove(p24)
            p2.remove(p24)
            return highercards(p1,p2)





p1count = 0
for i in range(1000):
    line = f.readline()
    c = line.split(" ")
    p1 = c[:5]
    p2 = c[5:]
    
    p2[4] =  p2[4][:2]
    print("i",i,p1,p2)
    p1ranking = ranking(p1)
    p2ranking = ranking(p2)
    print("p1",ranktoname(p1ranking),"p2",ranktoname(p2ranking))

    
    if p1ranking > p2ranking:
        print("p1better")
        p1count += 1
    elif p1ranking == p2ranking:
        print("tie")
        p1num = []
        p2num = []

        for i in range(5):
            p1num.append(p1[i][0])
            p2num.append(p2[i][0])
            p1num[i] = tonum(p1num[i])
            p2num[i] = tonum(p2num[i])
        
        if p1better(p1num,p2num,p1ranking):
            print("p1won")
            p1count += 1
        else:
            print("p2won")
    else:
        print("p2better")
print(p1count)

