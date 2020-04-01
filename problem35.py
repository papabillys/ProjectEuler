# Problem 35 - Circular primes
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
#
# Answer: 55


# Function that returns a list of primes found at stackoveflow.
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


# Returns a list of the circular forms of the number.
def get_circular(number):
    length = len(str(number))
    i = 0
    circular_list = [number]
    number = str(number)
    while i < length - 1:
        temp = number[1:length] + number[0]
        number = temp
        circular_list.append(int(number))
        i = i+1
    return set(circular_list)


# Returns true if all the digits of the number are odd numbers.
# If a digit is even number, then all the circulars of the number are not primes.
def check_number(number):
    all_odd = True
    number = set(str(number))
    for y in number:
        if int(y) % 2 == 0:
            all_odd = False
    return  all_odd


def problem35():

    # Get a list of primes below one million.
    limit = 1000000
    prime_list = primes(limit)

    # Counter is 1 because i count 2. Otherwise, 2 is not counter because of check_number
    counter = 1
    limit = len(prime_list)
    i = 0
    while i < limit:

        # Replace circular primes that already count with 0.
        if prime_list[i] != 0 and check_number(prime_list[i]):

            # Get a list of all the circular numbers of prime_list[i].
            circ = get_circular(prime_list[i])

            # Check if all circular numbers are primes.
            all_primes = True
            for x in circ:
                if x not in prime_list:
                    all_primes = False

            # Update counter
            if all_primes:

                # Update counter.
                counter = counter + len(circ)

                # Replace the circulars of the number from prime list with number 0.
                for y in circ:
                    index = prime_list.index(y)
                    prime_list[index] = 0

        i = i+1

    print(counter)


problem35()