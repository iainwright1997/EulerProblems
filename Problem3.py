# FIND THE LARGEST PRIME FACTOR OF 600851475143
from math import *


def prime_check(y):
    limit2 = floor(sqrt(y))
    count2 = 2
    check = 1
    while count2 <= limit2:
        if y % count2 == 0:
            check = 0
        count2 += 1
    return check


def largest_factor(x):
    limit1 = ceil(sqrt(x))
    count1 = 2
    prime_list = []
    while count1 <= limit1:
        if x % count1 == 0:
            if prime_check(count1) == 1:
                big_prime = count1
        count1 += 1
    return(big_prime)


print(largest_factor(600851475143))
