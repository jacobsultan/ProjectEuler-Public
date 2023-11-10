



def longdivision(top,bottom):
    arr = [top]
    ind = 0
    while(ind < 100):                      
        curr = arr[ind]        
        if curr == 0:
            break
        elif bottom > curr:
            arr.append(curr * 10)
            arr[ind] = 0
        else:
            place = int(curr / bottom)
            arr[ind] = place
            arr.append( (curr - arr[ind] * bottom) * 10)
            
        ind += 1
    return arr

fin = []

for a in range(10,100):
    print("")
    print(a)
    for b in range(10,100):

        if a >= b:
            continue
        sta = str(a)
        stb = str(b)
        if sta[0] != stb[0] and sta[1] != stb[0] and sta[0] != stb[1] and sta[1] != stb[1]:
            continue

        if a % 10 == 0 and b % 10 == 0:
            continue

        print("1", b)
        print(int(a / 10), int(b / 10))
        fir = longdivision(a,b)
        sec = longdivision(int(a / 10), int(b / 10))
        if fir == sec:
            print("found")
            fin.append((a,b))

        if b % 10 != 0:
            print("2",b)
            print(int(a / 10), b % 10)
            fir = longdivision(a,b)
            sec = longdivision(int(a / 10), b % 10)
            if fir == sec:
                print("found")
                fin.append((a,b))
            
        if b % 10 != 0:
            print("3",b)
            print(int(a % 10), int(b % 10))
            fir = longdivision(a,b)
            sec = longdivision(int(a % 10), int(b % 10))
            if fir == sec:
                print("found")
                fin.append((a,b))


        print("4",b)
        print("a",a,"b",b)
        print(int(a % 10), int(b / 10) )
        fir = longdivision(a,b)
        sec = longdivision(int(a % 10), int(b / 10))
        if fir == sec:
            print("found")
            fin.append((a,b))



       
print(fin)


42 / 84
24 / 48
21 / 42

15 / 75


16 / 64
26/65
19 / 95
49/98








