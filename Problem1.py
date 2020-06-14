# FIND THE SUM OF ALL MULTIPLES OF 3 AND 5 BELOW 100
x = 1
total = 0
while(x <= 999):
    if x % 3 == 0 or x % 5 == 0:
        total += x
    x += 1
print(total)
