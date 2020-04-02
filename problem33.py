# Problem 33 - Digit cancelling fractions
# The fraction 49/98 is a curious fraction,
# as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value,
# and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
#
# Answer: 100


# This function checks if a fraction is trivial.
def check_trivial(x, y):
    if x%10 == 0:
        if y % 10 == 0:
            return True
    return False


# This function checks if a fraction is curious.
def check_curious(x, y):

    temp_x = list(str(x))
    temp_y = list(str(y))
    first_fraq = x/y
    found_common_number = False
    for iter1 in temp_x:
        if iter1 in temp_y:
            found_common_number = True
            common = iter1

    if found_common_number:
        temp_x.remove(common)
        temp_y.remove(common)
        if int(temp_y[0]) != 0:
            frac = int(temp_x[0]) / int(temp_y[0])
            if frac == first_fraq:
                return True

    return False


# Function that returns a list of primes < n.
# This function found on stackoverflow.
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


# This function finds the lowest form of a fraction and returns the denominator.
def find_lowest_form(x, y):
    prime_list = primes(100)
    i = 0
    exit_flag = False
    while not exit_flag:
        while x % prime_list[i] == 0 and y % prime_list[i] == 0:
            x = x / prime_list[i]
            y = y / prime_list[i]

        if prime_list[i] > x or prime_list[i] > y:
            return y

        i = i+1

    # Returns 0 for error.
    return 0


def problem33():

    # Starting numbers would be numerator = 11 and denominator = 12.
    den = 12
    counter = 0
    total_num = 1
    total_den = 1
    while den < 100 and counter < 4:
        num = 11
        while num < den:
            if not check_trivial(num, den):
                if check_curious(num, den):
                    counter = counter+1
                    total_den = total_den * den
                    total_num = total_num * num
            num = num+1
        den = den+1

    # Got the fraction of 4 curious numbers : total_num / total_den.
    # Now i ll find its lowest form.
    print(total_num)
    print(total_den)
    lowest_den = find_lowest_form(total_num, total_den)
    print(lowest_den)


problem33()