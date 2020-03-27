# Problem 30 - Digit fifth powers
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#
# Answer: 443839

# 9^5 = 59049, 999999 sum is 354294 ( so max sum of a 6-digit number gives sum a 6-digit number )
# 9999999 = 413343 ( so max sum of a 7-digit number gives sum a 6-digit number )
# So my upper limit will be 9999999

import math


# Return true if the number can be written as the sum of fifth powers of their digit.
def check(number):
    num_str = str(number)
    num_str = list(num_str)
    sum = 0
    for x in num_str:
        temp = int(x)
        sum = sum + math.pow(temp, 5)

    if sum == number:
        return True
    else:
        return False


def problem30():
    limit = 9999999
    i = 2
    total = 0
    while i < limit:
        if check(i):
            total = total+i
        i = i+1
        print(limit-i)

    print(total)


problem30()