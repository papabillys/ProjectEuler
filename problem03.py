# Problem 3 - Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# Answer: 6857

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


def problem3():
    number = 600851475143 # number can be parameter
    listOfAllPrimes = []
    listOfPrimes = []
    divideFinished = False
    i = 0
    while not divideFinished:
        listOfAllPrimes = findNextPrime(listOfAllPrimes)
        if number % listOfAllPrimes[i] == 0 :
            number = number / listOfAllPrimes[i]
            listOfPrimes.append(listOfAllPrimes[i])
            if number == 1 :
                divideFinished = True
        else :
            i = i+1
    # print("List of primes : " , listOfPrimes)
    print("Largest prime is ", listOfPrimes[len(listOfPrimes)-1])


problem3()
