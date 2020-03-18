# Problem 21 - Amicable numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
#
# Answer: 31626

def problem21():
    # First i ll calculate the d(x) for each number
    number = 1
    mylist = []
    while number <= 10000 :
        i = 1
        sum = 0
        while i < number :
            if number%i == 0 :
                sum = sum+i
            i = i+1
        mylist.append(sum)
        number = number+1
    # Getting the sum of all amicable numbers
    i = 1
    lastSum = 0
    while i <= 10000 :
        temp = mylist[i-1]
        if len(mylist) >= temp -1 :
            if mylist[temp-1] == i and temp != i :
                lastSum = lastSum + i
        i = i+1

    print(lastSum)

problem21()