# FIND THE LARGEST PALINDROME THAT IS A PRODUCT OF TWO THREE-DIGIT NUMBERS
big_palindrome = 0
for a in range(100, 999):
    for b in range(100, 999):
        num = str(a*b)
        rev_num = num[::-1]
        if num == rev_num and int(num) >= big_palindrome:
            big_palindrome = int(num)


print(big_palindrome)
