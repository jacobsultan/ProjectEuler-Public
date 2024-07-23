def numtobin(integer):
    twofactor = 1
    while(2 ** (twofactor) <= integer):
        twofactor += 1
    length = twofactor
    bin = ""
    while(integer > 0):
        if 2 ** twofactor <= integer:
            bin += "1"
            integer -= 2 ** twofactor
        else:
            bin += "0"
        twofactor -= 1
    bin += (length - len(bin) + 1) * "0"
    return int(bin)