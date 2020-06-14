# FIND THE LOWEST NUMBER THAT IS DIVISIBLE BY ALL NUMBERS FROM 1 TO 20
from math import *

x = 20
s_number = 1


def prime_check(y):
    limit = floor(sqrt(y))
    count = 2
    check = 1
    while count <= limit:
        if y % count == 0:
            check = 0
        count += 1
    return check


for i in range(2, x):
    if prime_check(i) == 1:
        power = floor(log(x, i))
        value = i ** power
        s_number = s_number * value
print(s_number)
