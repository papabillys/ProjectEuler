# Problem 41 - Pandigital prime
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
#
# Answer: 7652413

# If the sum a numbers digits can be divided by 3, then the number can be dividen by 3.
# So if we consider all the digit combinations for pandigital primes then :
# 9 digit -> 1+2+3+4+5+6+7+8+9 = 45%3 = 0 , so cannot be pandigital
# 8 digit -> 1+2+3+4+5+6+7+8 = 36%3 = 0 , so cannot be pandigital
# 7 digit -> 1+2+3+4+5+6+7 = 28%3 > 0, so CAN BE PANDIGITAL
# 6 digit -> 1+2+3+4+5+6 = 21%3 = 0 , so cannot be pandigital
# 5 digit -> 1+2+3+4+5 = 15%3 = 0 , so cannot be pandigital
# 4 digit -> 1+2+3+4 = 10%3 > 0, so CAN BE PANDIGITAL
# 3 digit -> 1+2+3 = 6%3 = 0 , so cannot be pandigital
# 2 digit -> 1+2 = 3%3 = 0 , so cannot be pandigital
# So i ll check for pandigital primes first all the 7 digit numbers.
# If no prime found in 7-digit , i ll check 4-digit.

import time
list_of_primes = []


# This function checks if a number is pandigital or no.
def checkPandigital(number):
    num_str = str(number)
    digits = len(num_str)

    # 1-digit numbers are not pandigital.
    if digits == 1:
        return False

    num_str = list(num_str)

    # Check if list has duplicates. If there are duplicates, number is not pandigital.
    if len(num_str) != len(set(num_str)):
        return False

    # If the number has digit 0 then it is not pandigital.
    if str(0) in num_str:
        return False

    # If any digit in the list is greater than length of the number, then it is not pandigital.
    for x in num_str:
        if int(x) > digits:
            return False

    return True


# This function checks fast if a number can be prime or no.
# If returns true, number is not prime.
# If returns false, number might be prime, or might not.
def fastCheck(number):
    num_str = str(number)

    # Check if number is 1-digit. These rules do not apply to 1-digit numbers.
    if len(num_str) == 1:
        return False

    # Check if number is even or multiple of 5
    final_digit = int(num_str[len(num_str)-1])
    if final_digit % 2 == 0 or final_digit == 5:
        return True

    # If the sum of the digits of a number is multiple of 3, then the number is divided by 3
    sum = 0
    for x in num_str:
        sum = sum + int(x)
    if sum % 3 == 0:
        return True

    return False


# This function finds the next prime of list_of_primes
def nextPrime():

    global list_of_primes
    n = len(list_of_primes)

    prime_found = False
    i = list_of_primes[n - 1] + 1

    while not prime_found:
        if fastCheck(i):  # Its not a prime
            i = i + 1
        else:  # Might be prime
            j = 0  # variable for running through prime list to check if num is prime or not
            flag_check = True  # flag if i is divided with a prime of list
            flag_limit = True  # flag will become false when j>n or 2*x[j] > i

            while flag_limit and flag_check:

                # Check if j is on index limits
                if j < n:
                    if list_of_primes[j-1] > 10:

                        # Check if prime number is bigger than i/2 . If so , we stop searching for factors of i.
                        if 2*list_of_primes[j-1] > i:
                            flag_limit = False

                    # Check if i is divided
                    if i % list_of_primes[j] == 0:
                        flag_check = False
                    else:
                        j = j + 1
                else:
                    flag_limit = False

            if flag_check:  # j is not divided by any number in the list, so it is prime.
                prime_found = True
            else:  # j is not prime.
                i = i + 1

    return i


def checkPrime(number):
    global list_of_primes
    i = 0
    while i < len(list_of_primes) and 2*list_of_primes[i] < number:
        if number % list_of_primes[i] == 0:
            return False
        else:
            i = i+1
    return True


def problem41():

    start = time.time()

    max_pandigital = 7654321
    min_pandigital = 1234567

    # I will need a list of primes with upper limit max_pandigital/2
    if len(list_of_primes) == 0 :
        list_of_primes.append(2)

    while list_of_primes[len(list_of_primes)-1] < max_pandigital//2:
        prime_num = nextPrime()
        list_of_primes.append(prime_num)

    # Searching for pandigital prime with 7 digits
    i = max_pandigital
    found7Flag = False
    while i > min_pandigital and not found7Flag:
        if checkPandigital(i):
                checkPrime(i)
                found7Flag = True
        i = i-1

    # We got a 7digit pandigital
    if found7Flag:
        print(i+1)
    else:
        # Searching for 4-digit pandigital
        max_pandigital = 4321
        min_pandigital = 1234
        i = max_pandigital
        found4Flag = False
        while i > min_pandigital and not found4Flag:
            if checkPandigital(i):
                if i in list_of_primes:
                    found4Flag = True
            i = i-1

        # We got a 4digit pandigital
        if found4Flag:
            print(i+1)
        else:
            print("No pandigital prime found.")

    print("Running time: ", time.time() - start )


problem41()
