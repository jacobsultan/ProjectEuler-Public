squaredict = {}
import time
start_time = time.time()

xfins = []

def closest(x,d,miny):

    if x not in squaredict:
        squaredict[x] = x ** 2

    target = squaredict[x]

    
    maxy = x 
    if x > 1000:
        maxy = max(x,miny + 1000)
    if x > 100000:
        maxy = miny + 2
    
    if x > 3000000:
        if abs(target - ((miny + 1) ** 2 * target)) < abs(target - (miny ** 2 * target)):
                return miny + 1
        else:
            return miny
        maxy = miny + 1
    
    if miny not in squaredict:
        squaredict[miny] = miny ** 2
    if miny + 1 not in squaredict:
        squaredict[miny + 1] = (miny + 1) ** 2

    
        

    notfound = True
    while notfound and miny < maxy:
        if x > 8000000:
            xfins.append(d)
            return -1
            break
        test =int( (miny + maxy) / 2)

        if test not in squaredict:
            squaredict[test] = test ** 2
        if test == miny:
            if x % 1000000 == 0:
                print("x",x,"target",target,"miny",(miny ** 2) * d,"miny + 1", (miny + 1) ** 2  * d)
            if abs(target - ((miny + 1) ** 2 * target)) < abs(target - (miny ** 2 * target)):
                return miny + 1
            else:
                return miny
        
        teststat = squaredict[test] * d
 

        if squaredict[test] * d + 1 == target:
            return test
            notfound = False
            break
        elif squaredict[test] * d < target:
            miny = test
        else:
            maxy = test
         


def findx(d):
    found = False
    x = 2
    start = 0

    while(not found and start < x):
        a = closest(x,d,start)
        if a == -1:
            return 1
        if squaredict[a] * d - squaredict[x] == -1:
            print("x",x,"y",a,"d",d)
            return x
            found = True
        else:
            start = a
            x += 1
        
        



maxxval = 0
maxd = 0
for i in range(200,300):
    print(xfins)
    if (i **0.5).is_integer():
        continue
    xval = findx(i)

    if xval > maxxval:
        maxxval = xval
        maxd = i

print("fin x val", maxxval, "fin d val",maxd)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
"""to try 





181

191

193

202

211

214

229

233

239

241

249

250

253
261
262
265
268
271
281
283
284
293
298
"""
