def numtobin(integer):
    twofactor = 1
    length = 0
    while(2 ** (twofactor ) <= integer):
        twofactor += 1
    arr = []
    while(integer > 0):
        if integer >= 2 ** twofactor:
            if length != 0:
                arr[length - twofactor] = 1
            else:
                arr.append(1)
                for i in range(twofactor):
                    arr.append(0)
                length = twofactor
            integer -= 2 ** twofactor
        twofactor -= 1
    return arr

def palin(number):
    string = str(number)
    arr = []
    for let in string:
        arr.append(let)
    low = 0
    high = len(arr) - 1
    while low < high:
        if arr[low] != arr[high]:
            return False
        low += 1
        high -=1
    return True

def palind(number):
    
    low = 0
    high = len(number) - 1
    while low < high:
        if number[low] != number[high]:

            return False
        low += 1
        high -=1
    return True

ret = []
for i in range(1,1000000):
    if i % 10000 == 0:
        print("i",i / 10000)
    if palin(i):
        if palind(numtobin(i)):

            ret.append(i)
print(ret)
print(sum(ret))
print("sum")