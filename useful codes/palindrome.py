def palindrome(number):
    return str(number)[::-1] == str(number) and str(number)[::-1][0] != '0'