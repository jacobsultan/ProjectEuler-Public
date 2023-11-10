notfound = True
og = 1
while(notfound):
    if og % 1000 == 0:
        print(og)
    ogstr = str(og)
    oggroup = set()
    for let in ogstr:
        oggroup.add(let)
    doublegroup = set()
    for let in str(og * 2):
        doublegroup.add(let)
    if len(oggroup.difference(doublegroup)) == 0 and len(doublegroup.difference(oggroup)) == 0:
        triplegroup = set()
        for let in str(og * 3):
            triplegroup.add(let)
        if len(oggroup.difference(triplegroup)) == 0 and len(triplegroup.difference(oggroup)) == 0:
            quadgroup = set()
            for let in str(og * 4):
                quadgroup.add(let)
            if len(oggroup.difference(quadgroup)) == 0 and len(quadgroup.difference(oggroup)) == 0:
                print("5step",og)
                quintgroup = set()
                for let in str(og * 5):
                    quintgroup.add(let)
                if len(oggroup.difference(quintgroup)) == 0 and len(quintgroup.difference(oggroup)) == 0:
                    print("6step",og)
                    sexgroup = set()
                    for let in str(og * 6):
                        sexgroup.add(let)
                    if len(oggroup.difference(sexgroup)) == 0 and len(sexgroup.difference(oggroup)) == 0:
                        notfound = False
                        print("DONE")
                        print(og)
    og += 1

