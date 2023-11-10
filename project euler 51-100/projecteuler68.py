results = {}
def produceline(num,outering,innerring):
    return[outering[num % 5],innerring[num % 5],innerring[(num + 1) % 5]]
def linecalc(num,outerring,innerring):
    tot = outerring[num] + innerring[num] + innerring[(num + 1) % 5]
    return tot
def tostring(outering,innerring):
    retstring = ""
    min = 11
    ind = -1
    for i in range(5):
        if outering[i] < min:
            min = outering[i]
            ind = i


    for i in range(5):
        line = produceline(i + ind,outering,innerring)
        for let in line:
            retstring += str(let)
    return retstring

outer = [10]
inner = []
used = set()
used.add(10)

def fill(target):
    if len(outer) == len(inner) == 5:
        works = True
        for i in range(5):
            if linecalc(i,outer,inner) != target:
                works = False
        if works:
            if target in results:
                results[target].append(tostring(outer,inner))
            else:
                results[target] = [tostring(outer,inner)]

    else:
        if len(outer) == 5:
            for i in range(1,10):
                if i not in used:
                    used.add(i)
                    inner.append(i)
                    innerlen = len(inner)
                    if innerlen != 1:
                        if linecalc(innerlen - 2,outer,inner) == target:
                            fill(target)
                    else:
                        fill(target)
                    inner.pop()
                    used.remove(i)

        else:
            for j in range(1,10):
                if j not in used:
                    used.add(j)
                    outer.append(j)
                    fill(target)
                    outer.pop()
                    used.remove(j)


    

for tot in range(11,30):
    print("tot",tot)    
    fill(tot)

max = 0
print(results)
for result in results:
    for item in results[result]:
        if int(item) > max:
            max = int(item)
print(max)
print(len(str(max)))
print("done")


"""
{14: ['1013635752824941', '1031914842725653'], 16: ['1015259493637871', '1051817673439295']}
"""