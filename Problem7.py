from math import *


def prime_check(y):
    limit = floor(sqrt(y))
    count = 2
    check = 1
    while count <= limit:
        if y % count == 0:
            check = 0
        count += 1
    return check


i = 1
x = 1
while i <= 10001:
    x += 1
    if prime_check(x) == 1:
        i += 1

print(x)


