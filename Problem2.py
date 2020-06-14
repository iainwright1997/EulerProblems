x = 1
y = 2
total = 0

while y <= 4000000:
    if y % 2 == 0:
        total += y
    x_temp = x
    x = y
    y = x + x_temp

print(total)