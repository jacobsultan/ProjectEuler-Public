string = "0."
for i in range(1,1000002):
    string += str(i)
a = int(string[1000000 + 1]) * int(string[100001])  * int(string[10001]) * int(string[1001])
a *= int(string[101]) * int(string[11]) * int(string[2])
print(a)
