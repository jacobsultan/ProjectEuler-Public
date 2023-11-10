import time
timenow = time.time()


mapping = {}
mapping[0] = 0
mapping[1] = len("one")
mapping[2] = len("two")
mapping[3] = len("three")
mapping[4] = len("four")
mapping[5] = len("five")
mapping[6] = len("six")
mapping[7] = len("seven")
mapping[8] = len("eight")
mapping[9] = len("nine")
mapping[10] = len("ten")
mapping[11] = len("eleven")
mapping[12] = len("twelve")
mapping[13] = len("thirteen")
mapping[14] = len("fourteen")
mapping[15] = len("fifteen")
mapping[16] = len("sixteen")
mapping[17] = len("seventeen")
mapping[18] = len("eighteen")
mapping[19] = len("nineteen")
mapping[20] = len("twenty")
mapping[30] = len("thirty")
mapping[40] = len("forty")
mapping[50] = len("fifty")
mapping[60] = len("sixty")
mapping[70] = len("seventy")
mapping[80] = len("eighty")
mapping[90] = len("ninety")
mapping[100] =len("hundred")
mapping[1000] = len("thousand")

n = 1
tot = 0
while(n <= 999):
    curr = n
    if curr < 21:
        tot += mapping[curr]
    elif curr < 100:
        currun = curr % 10
        currten = curr - currun
        tot += mapping[currun]
        tot += mapping[currten]
    
    else:
        if curr % 100 == 0:
            tot += mapping[100]
            tot += mapping[curr / 100]

        elif curr % 100 < 21:
            currdos = curr % 100
            currhun = curr - currdos
            tot += mapping[currdos]
            tot += mapping[100]
            tot += 3
            tot += mapping[currhun / 100]

        else:
            currun = curr % 10
            currten = (curr % 100) - currun
            currhun = curr - currten - currun
            tot += mapping[currun]
            tot += mapping[currten]
            tot += 3
            tot += mapping[100]
            tot += mapping[currhun / 100]
    n += 1



tot += 11
print(tot)

print(time.time() - timenow)


