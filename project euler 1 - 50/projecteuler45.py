
pent = []
for i in range(10000000):
    pent.append(i * (3 * i - 1)/2)
pentset = set(pent)
hex = []
for i in range(10000000):
    hex.append(i * (2* i - 1))
hexset = set(hex)
for i in range(10000000):
    tri = (i * (i+1)/2)
    if tri in hexset and tri in pentset:
        print(i, tri)
