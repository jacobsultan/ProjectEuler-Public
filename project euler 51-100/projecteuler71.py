small = 1
smallind1 = 0
smallind2 = 0
for i in range(1,1000000):
    if i % 1000 == 0:
        print("i",i)
    for j in range(int((i * 3) / 7) - 3, int((i * 3) / 7) + 3):
        curr = ((3 / 7) - (j / i))
        if  curr > 0 and curr < small:
            smallind1 = i
            smallind2 = j
            small = curr
print(smallind1,smallind2)

