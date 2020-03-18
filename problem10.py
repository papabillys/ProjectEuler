# Problem 10 - Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#
# Answer: 142913828922

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


def problem10():
    last = 0
    primeList = []
    sum = 0
    while last < 2000000: # 2000000 can be parameter
        primeList = findNextPrime(primeList)
        last = primeList[len(primeList)-1]
        sum = sum + last
        print(2000000-last) # Just to "know the progress"
    print("Sum is : ", sum-last)
    # Ans is : 142913828922


problem10()