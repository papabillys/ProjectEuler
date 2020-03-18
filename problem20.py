# Problem 20 - Factorial digit sum
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
#
# Answer: 648

def problem20():
    # First calculate the 100!
    i = 1
    number = 1
    while i <= 100 :
        number = number * i
        i = i + 1
    #Calculate the sum of the digits
    totalSum = 0
    temp = number
    while  temp > 10 :
        rem = temp % 10
        totalSum = totalSum + rem
        temp = temp // 10

    totalSum = totalSum + temp
    print("Total sum = ", totalSum)


problem20()