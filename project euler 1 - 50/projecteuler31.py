coins = []
coins.append(1)
coins.append(2)
coins.append(5)
coins.append(10)
coins.append(20)
coins.append(50)
coins.append(100)
coins.append(200)
print(coins)
way = []
def ways(curr,maxind):
    if curr == 200:
        way.append(1)
    elif curr < 200:
        for i in range(maxind,8):
            if coins[i] + curr <= 200:
                ways(curr + coins[i],i)
ways(0,0)
print(len(way))

