# Problem 40 - Champernowne's constant
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.12345678910-1-112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
#
# Answer: 210

def problem40():

    # 10th digit is the 9th char in string so i ll have starting string as number_str="0"
    number_str = "0"

    # Get the 1000000 digit string
    limit = 1000000
    i = 1
    while len(number_str) <= limit:
        number_str = number_str + str(i)
        i = i+1

    # Calculate the expression
    total = 1
    i = 1
    pos = 1
    print("")
    while i<=7:
        total = total * int(number_str[pos])
        i = i+1
        pos = pos * 10

    print(total)


problem40()