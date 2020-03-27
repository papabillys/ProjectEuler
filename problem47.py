# Problem 47 - Distinct primes factors
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
#
# Answer: 134043

import time
list_of_primes = []

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

    if n == 0:
        return 2

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


# This function checks if a number has 4 distinct prime factors
def has_four_distinct_prime_factors(number):
    global list_of_primes
    distinct_prime_factors = []
    i = 0
    exitFlag = False
    while not exitFlag:
        x = list_of_primes[i]

        # Check if a certain prime is factor of the number
        if number % x == 0:
            distinct_prime_factors.append(x)

        # Number has not 4 prime factor
        if x >= number:
            exitFlag = True

        # Number has at least 4 prime factors
        if len(distinct_prime_factors) == 4:
            exitFlag = True

        i = i+1

        # Making sure we wont get index out of boundaries error
        if len(list_of_primes) == i:
            next_prime = nextPrime()
            list_of_primes.append(next_prime)

    if len(distinct_prime_factors) == 4:
        return True
    else:
        return False


def problem47():

    start = time.time()
    global list_of_primes
    list_of_primes.append(2)

    # Filling list_of_primes with 100 prime numbers for start
    i = 0
    while i < 100:
        temp = nextPrime()
        list_of_primes.append(temp)
        i = i+1

    # Finding the 4 consecutive numbers
    numbers = []
    i = 2
    while len(numbers) < 4:
        if has_four_distinct_prime_factors(i):
            numbers.append(i)
            if len(numbers)>1:
                # diff must be 1 if numbers are consecutive
                diff = i - numbers[len(numbers)-2]
                if diff != 1:
                    numbers = []
                    numbers.append(i)
        i = i+1

    print(numbers)
    print("running time: ", time.time() - start )


problem47()