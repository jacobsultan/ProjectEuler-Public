
maxloop = 0
d = 0

for i in range(3,1001):
    print("")
    print("i = ", i)
    ind = 0
    arr = [1]
    pattern = False
    kk = 1
    startingvalue = -1
    startind = []
    while(not pattern):
        if ind == 10:
            startingvalue = arr[9]
        elif ind > 9:
            for val in startind:
                if arr[(ind - 1) - val + 9] != arr[ind - 1]:
                    startind.remove(val)
            if arr[ind - 1] == startingvalue:
                if len(startind) > 0:
                    test = startind.pop()


                    if test - 9 > maxloop:

                        maxloop = test - 9
                        d = i
                    pattern = True
                else:
                    startind.append(ind - 1)



                
            
          

        kk += 1
        curr = arr[ind]        
        if curr == 0:
            print("break for 0")
            break
        elif i > curr:
            arr.append(curr * 10)
            arr[ind] = 0
        else:
            place = int(curr / i)
            arr[ind] = place
            arr.append( (curr - arr[ind] * i) * 10)
            
        ind += 1
    print(arr)
print("done")
print(d)


