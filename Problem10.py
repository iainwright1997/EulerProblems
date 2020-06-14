# FIND THE SUM OF ALL PRIMES BELOW 2,000,000

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


sum = 0
for i in range(2, 2000000):
    if prime_check(i) == 1:
        sum += i

print(sum)
