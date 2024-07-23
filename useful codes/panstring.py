pans = []
def place(string,top):
    if len(string) == top:
        pans.append(string)
    else:
        for i in range(1,top + 1):
            if str(i) not in string:
                place(string + str(i),top)

place("", 7)
print(pans)