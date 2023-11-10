
  
def foundloop(array):
    loopstart = array[5]
    ind = 6
    while ind < len(array):
        if array[ind] == loopstart:
            b = test(array,ind)
            if b:
                return ind - 5
                break
            
        ind += 1
    return False
        

def test(array,ind):

    for i in range((ind - 5) * 8):
        if ind + i >= len(array):
            return False
        if array[ind + i] != array[5 + i]:
            return False
    return True

    


def sharefactor(n1,n2,n3):
    if abs(n1) == 1 or abs(n2) == 1 or abs(n3) == 1:
        return False
    else:
        if abs(n1) <= abs(n2) and abs(n1) <= abs(n3):
            return n1
        elif abs(n2) <= abs(n1) and abs(n2) <= abs(n3):
            return n2
        else:
            return n3


def nextperiod(sqrt,prevsqrtfactor,other,prevbottom):
    bottom = sqrt - other ** 2
    topsqrt = sqrt 
    sqrtfactor = prevsqrtfactor * prevbottom
    topother = - other * prevbottom
    remainder =int( (int(topsqrt ** 0.5) * sqrtfactor + topother) / bottom)
    topother = topother - remainder * bottom
    k = sharefactor(sqrtfactor,topother,bottom)
    if k:
        sqrtfactor /= k
        topother /= k
        bottom /= k
    return [topsqrt,sqrtfactor,topother,bottom,remainder]
 

def oddperiod(number):
    start = number ** 0.5
    if start.is_integer():
        return False
    start = int(start)
    noloop = True
    a = [number,1,-start,1]
    loop = []
    counter = 0
    while noloop:
        counter += 1
        a = nextperiod(a[0],a[1],a[2],a[3])
        remain = a[4]
        loop.append(remain)
        if counter % 12 == 0:
            c = foundloop(loop)
            if c:
                if c % 2 == 0:
                    return False
                else:
                    return True
                noloop = False
                break



tot = 0
for i in range(2,10001):
    print(i)
    if oddperiod(i):
        tot += 1
print(tot)

