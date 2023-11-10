found = False
length = 2
k = 1
while not found:
    cubes = []
    lower = 10 ** length
    higher = 10 ** (length + 1)
    for i in range(int(lower ** (1/ 3)) - 1, int((higher) ** (1 / 3)) + 1):
        if higher > i ** 3 >= lower:
            cubes.append( i ** 3)
    print(len(cubes))
    badlist = set()

    for i in range(len(cubes)):
        if cubes[i] not in badlist:
            ogsetnums = set()
            setofothers = set()
            setofothers.add(cubes[i])
            lets = []
            for let in str(cubes[i]):
                lets.append(let)
                ogsetnums.add(let)
            for j in range(i + 1, len(cubes)):
                currset = set()
                if cubes[j] not in badlist:
                    for let in str(cubes[j]):
                        currset.add(let)
                    if len(currset) == len(ogsetnums):
                        empty = set()
                        if currset.difference(ogsetnums) == ogsetnums.difference(currset):
                            newlet = []
                            for let in lets:
                                newlet.append(let)
                            for let in str(cubes[j]):
                                if let in newlet:
                                    newlet.remove(let)
                                if len(newlet) == 0:
                                    setofothers.add(cubes[j])
                                    if len(setofothers) == 5:
                                        print(currset)
                                        print(ogsetnums)
                                        print(currset.difference(ogsetnums))
                                        print(ogsetnums.difference(currset))
                                        print("")
                                        print("")
                                        print("DONE")
                                        print("setofothers",setofothers)
                                        found = True
                                        break
            
        for wronguns in setofothers:    
            badlist.add(wronguns)
        

    length += 1

