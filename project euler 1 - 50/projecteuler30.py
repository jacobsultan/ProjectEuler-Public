

from operator import truediv
from unittest import skip

ret = []
for i in range(1,3000000):
    
    skipper = False
    target = i
    string = str(target)
    for let in string:
        if int(let) > 4:
            skipper = True
        if int(let) == 9:
            if i < 59000:
                skipper = False
                break

        elif int(let) > 7:
            if i < 32000:
                skipper = False
                break
    if not skipper:
        continue
    tot = 0
    for let in string:
        tot += int(let) ** 5
    if tot == target:
        print("yes",target)
        ret.append(target)
print(ret)

    


