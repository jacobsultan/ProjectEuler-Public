tot = 1
curr = 1
k = 1
for i in range(501):
        for i in range(4):
            curr += 2 * k
            print(curr)
            tot += curr
        k += 1
print(tot)