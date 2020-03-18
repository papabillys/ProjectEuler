# Problem 16 - Power digit sum
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
#
# Answer: 1366

def problem16():
    # Find 2^1000
    i = 1
    number = 2
    while i < 1000 : # 1000 can be parameter
        number = number*2
        i = i+1
    print("Number is ", number)

    # Find the sum of its digits
    sum = 0
    while number/10 >= 1:
        add = number%10
        sum = sum+add
        number = number//10
    sum = sum+number
    print("Sum is ",sum)



problem16()