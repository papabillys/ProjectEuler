# Problem 1 - Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168

def problem1():
    i, sum = 0, 0
    mult3, mult5 = False, False
    while i < 1000: # 1000 can be a parameter
        if i % 3 == 0 :
            mult3 = True
        if i % 5 == 0 :
            mult5 = True
        if mult3 or mult5 :
            sum = sum + i
        i = i + 1
        mult5 = False
        mult3 = False
    print("Sum is: ", sum)

problem1()