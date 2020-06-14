# FIND THE DIFFERENCE BETWEEN THE SQUARE OF THE SUM FROM 1 TO 101 AND THE SUM OF SQUARES FROM 1 TO 101
sum_square = 0
sum = 0
for i in range(1, 101):
    sum_square += (i ** 2)
    sum += i
square_sum = sum ** 2
print(square_sum - sum_square )
