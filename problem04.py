# Problem 4 - Largest palindrome product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609
# Largest product of two 3-digit numbers is 999 x 999 = 998001 so this will be my upper limit
# Smallest product of two 3-digit numbers is 100 x 100 = 10000 so this will be my down limit

# Function to check if a number is palindromic
def isPalindomic(number):
    number_str = str(number)
    digits = len(number_str)
    number_str = list(number_str)

    i = 0
    j = digits-1
    pal_flag = True
    while i<j and pal_flag:
        if number_str[i] != number_str[j]:
            pal_flag = False
        i = i+1
        j = j-1

    return pal_flag

# Function which finds if a number is product of two 3-digit numbers.
# Returns 0 if the number isnt product else returns one of the two products ( largest one )
def findProducts(number):
    i = 999
    while i > 100:
        j = 999
        exit_flag = False
        while not exit_flag:
            if i*j > number:
                j = j-1
                if j < 100:
                    exit_flag = True
            elif i*j == number:
                return i
            else:
                exit_flag = True
        i = i-1
    return 0


def problem4():
    upper_limit = 998001
    down_limit = 10000
    i = upper_limit
    exit_flag = False
    while i > down_limit and not exit_flag:
        if isPalindomic(i):
            x = findProducts(i)
            if x == 0:
                i = i-1
            else:
                exit_flag = True
        else:
            i = i-1
    print(i)


problem4()
