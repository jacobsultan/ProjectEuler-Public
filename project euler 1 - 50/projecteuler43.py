pans = []
def place(string,top):
    if len(string) == top:
        pans.append(string)
    else:
        for i in range(0,top):
            if str(i) not in string:
                place(string + str(i),top)

place("",10)

print(len(pans))
tot = 0

for pan in pans:
    if int(pan[1:4]) % 2 != 0:
        continue
    if int(pan[2:5]) % 3 != 0:
        continue
    if int(pan[3:6]) % 5 != 0:
        continue
    if int(pan[4:7]) % 7 != 0:
        continue
    if int(pan[5:8]) % 11 != 0:
        continue
    if int(pan[6:9]) % 13 != 0:
        continue
    if int(pan[7:10]) % 17 != 0:
        continue

    print(pan)
    tot += int(pan)

print(tot)
