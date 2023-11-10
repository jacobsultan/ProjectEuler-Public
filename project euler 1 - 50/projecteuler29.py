twos = "2,4,8,16,32,64"
twosdup = 0 
twos = set()
threes = "3,9,27,81"
threesdup = 0
threes = set()
fives = "5,25"
fivesdup = 0
fives = set()
sixes = "6,36"
sixes = set()
sevens = "7,49"
sevens = set()
tens = "10,100"
tens = set()
for j in range(1,7):
    k = 2 ** j
    print("k",k)
    for i in range(2,101):
        if i * j in twos:
            twosdup += 1
        twos.add(i * j)
print("two",twosdup)

for j in range(1,5):
    k = 3 ** j
    print("k",k)

    for i in range(2,101):
        if i * j in threes:
            threesdup += 1
        threes.add(i * j)
print("threes",threesdup)

for j in range(1,3):
    k = 5 ** j
    print("k",k)

    for i in range(2,101):
        if i * j in fives:
            fivesdup += 1
            print("i*k",i)
        fives.add(i * j)
kss = list(fives)
kss.sort()
print(kss)
print("fives",fivesdup)


        

tot = 99 ** 2 - twosdup - threesdup - 4 * fivesdup
print(tot)