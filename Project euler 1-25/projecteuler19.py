import time
currtime = time.time()

months = {}
months[1] = 31
months[2] = 29
months[3] = 31
months[4] = 30
months[5] = 31
months[6] = 30
months[7] = 31
months[8] = 31
months[9] = 30
months[10] = 31
months[11] = 30
months[12] = 31

month = 1
year = 1900
day = 7
while(year == 1900):
    day += 7
    if day > months[month]:
        month += 1
        day = day - months[month - 1]
        if month == 13:
            break


day = 5
month = 1
year = 1901

tot = 0

while(year < 2001):
    if day == 1:
        tot += 1
    day += 7
    if day > months[month]:
        month += 1
        day = day - months[month - 1]
        if month == 13:
            month = 1
            year += 1
            if year % 4 == 0:
                months[2] = 29
            else:
                months[2] = 28


print(tot)

print(time.time() - currtime)
