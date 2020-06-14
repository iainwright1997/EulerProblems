from math import *

for a in range(1, 500):
    for b in range(1, 500):
        for c in range(1, 500):
            if a + b + c == 1000:
                if c == sqrt(b ** 2 + a ** 2):
                    product = a * b * c

print(product)