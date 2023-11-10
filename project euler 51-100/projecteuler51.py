def fill(totxs,currxs,size,curr):
    if len(curr) == size:
        if currxs == totxs:
            options.append(curr)

    else:
        if currxs < totxs:
            currx = curr + "x"
            curry = curr + "y"
            fill(totxs,currxs + 1,size,currx)
            fill(totxs,currxs,size,curry)


        else:
            curr += "y"
            fill(totxs,currxs,size,curr)
primes = [2]
lastprime = 1

for i in range(2,3300):
    temp = i
    for prime in primes:
        if temp < lastprime:
            break
        elif prime ** 2 > i:
            if temp == i:
                primes.append(temp)
                lastprime = temp
            temp = 1
            break
        while (temp / prime).is_integer():
            temp = temp / prime

primes[0] = 2
primeset = set(primes)

def isprime(integer):
    for prime in primes:
        if (integer / prime).is_integer():
            return False
        if prime ** 2 > integer:
            return True
    return True

xmap = {}

def test(string,curr,og):
    if curr == len(og):
        xs = xmap[og]
        counter = 0
        for i in range(10):
            newstring = ""

            if counter >= 3:
                break
            newind = 0
            for k in range(curr):
                if k in xs:
                    newstring += str(i)
                else:
                    newstring += string[newind]
                newind += 1
            
            if curr - 1 in xs:
                if newstring[-1] in {"0","2","4","6","8"}:
                    counter += 1

            elif newstring[-1] in {"0","2","4","6","8"}:
                counter = 3
            elif not isprime(int(newstring)):
                counter += 1

        if counter < 3:
            print("DONE")
            print("og",og)
            print("string",string)
    else:
        if og[curr] == "x":
            string  += "x"
            test(string,curr + 1,og)
        else:
            for i in range(10):
                newstring = string + str(i)
                test(newstring,curr + 1,og) 

            




for length in range(3,8):
    print("")
    print("length",length)
    for i in range(1,length + 1):
        variables = i
        others = length - i
        carryon = True
        options = []
        fill(variables,0,length,"")
        for option in options:
            for i,let in enumerate(option):
                if let == "x":
                    if option in xmap:
                        xmap[option].append(i)
                    else:
                        xmap[option] = [i]

        for option in options:
            print("")
            print(option)

            test("",0,option)


print("done")