# Problem 45 - Triangular, pentagonal, and hexagonal
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.
#
# Answer: 1533776805

import math

# Check if number is triangle
# Actually i form formula as a quadratic equation ( n^2 +n -2*number = 0 )
# Then i solve this equation finding a,b,c ( a*n^2 + b*n + c = 0 )
def checkTriangle(number):

    # d = b^2 - 4*a*c
    d = 1+8*number

    # Get the square root of d
    d = math.sqrt(d)
    if d.is_integer():

        # x1,x2 = (-b +- square_root_of_d) / 2*a but i want to keep the result>0 so
        # x = ( -b + square_root_of_d ) / 2*a
        x = (d-1) / 2
        if x.is_integer():
            return True
        else:
            return False
    else:
        return False

# Using the same logic as checkTriangle with quadratic equation 3*n^2 -n -2*number = 0
def checkPentagonal(number):
    d = 1+24*number
    d = math.sqrt(d)
    if d.is_integer():
        x = (d+1) / 6
        if x.is_integer():
            return True
        else:
            return False
    else:
        return False

# Check if a number is triangle and pentagonal.
# The number given as parameter is hexagonal
def checkNumber(number):
    if checkTriangle(number):
        if checkPentagonal(number):
            return True

    return False


def problem45():
    exitFlag = False
    i = 1
    while not exitFlag:
        hex = i * ( 2*i-1 )
        if hex > 40755:
            if checkNumber(hex):
                exitFlag = True
        i = i+1
    print(hex)


problem45()