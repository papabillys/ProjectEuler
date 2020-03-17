# Problem 6 - Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
#Answer: 25164150

def problem6():
    sum = 0
    sumSquares = 0
    i = 0
    while i <= 100: # 10 can be parameter
        sum = sum + i
        sumSquares = sumSquares + i**2
        i = i+1
    sum = sum**2
    print("Sum total square = ", sum)
    print("Sum seperate squares = ", sumSquares)
    print("Total - sep = ", sum-sumSquares)


problem6()