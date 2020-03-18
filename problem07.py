# Problem 7 - 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
#
# Answer: 104743

def findNextPrime(x): # x is a list with prime numbers, finds the next one, adds it to the list and returns the list
    n = len(x)
    if n == 0 :
        x = [2]
    else :
        i = x[n-1] + 1 # i is the number i ll +1 till i find a prime
        primeFound = False
        while not primeFound:
            j = 0 # running through prime list to check if num is prime or not
            flag = True # flag if i is divided with a prime of list
            while j<n and flag :
                if i % x[j] == 0 :
                    flag = False
                else :
                    j = j+1
            if flag :
                primeFound = True
            else :
                i = i+1
        x.append(i)
    return x


def problem7():
    primes = []
    while len(primes) < 10001: # 10001 can be parameter
        primes = findNextPrime(primes)
    print("The 10001th prime is ", primes[len(primes)-1])


problem7()
