choices = {}

def choose(poss,ask,curr):
    if len(curr) == ask:
        choices[poss][ask].append(curr)
    else:
        if len(curr) == 0:
            for i in range(0,poss):
                curr += str(i)
                choose(poss,ask,curr)
                curr = ""
        else:
            for i in range(int(curr[-1]) + 1, poss):
                curr += str(i)
                choose(poss,ask,curr)
                curr = curr[:len(curr) - 1]



for i in range(1,8):
    bigger = []
    for j in range(0,i + 1):
        now = []
        bigger.append(now)
    choices[i] = bigger


for i in range(1,8):
    for j in range(1,i + 1):
        choose(i,j,"")
   
print(choices)



#permutations
from itertools import permutations

def generate_numbers(digits):
    perm = permutations(digits)    
    numbers = []
    for p in perm:
        num = int(''.join(map(str, p)))
        numbers.append(num)
    return numbers

# Example usage
digits = [1, 2, 3]
generate_numbers(digits)