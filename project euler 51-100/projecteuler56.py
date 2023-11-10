

max = 0
for j in range(1,100):
    for i in range(100):
        biggie = str(j ** i)
        summ = 0
        for let in biggie:
            summ += int(let)
        if summ > max:
            max = summ
print(max)