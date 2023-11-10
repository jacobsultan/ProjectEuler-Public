lychrel = {}
for i in range(1,10000):
    print("")
    print("i",i)
    curr = i
    attempts = 0
    while(attempts < 51):
        back = int(str(curr)[::-1])
        new = curr + back
        if str(new) == str(new)[::-1]:
            break
        curr = new
        attempts += 1
    lychrel[i] = attempts

counter = 0
for i in range(1,10000):
    if lychrel[i] == 51:
        counter += 1
print(counter)



