# Problem 36 - Double-base palindromes
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
#
# Answer: 872187

def binaryMaker(number):

    x = number
    flagReady = False
    binaryNumber = 0
    binaryList = []

    # First i append to a list the remainings of number%2 which is the binary number backwards
    while not flagReady:
        temp = x % 2
        binaryList.append(temp)
        x = x // 2
        if x == 0 :
            flagReady = True

    # I read the binary from end to start which is the normal binary number
    j = len(binaryList) - 1
    while j >= 0 :
        binaryNumber = binaryNumber + binaryList[j]
        binaryNumber = binaryNumber * 10
        j = j-1

    binaryNumber = binaryNumber // 10
    return binaryNumber

def checkPalindromic(number):

    x = number
    length = len(str(x))

    # First i split the number into a list which displays the number backwards
    i = 0
    numList = []
    while i < length-1 :
        temp = x % 10
        numList.append(temp)
        x = x // 10
        i = i+1
    numList.append(x)

    # Get the limits till the mid of the list
    if length % 2 == 0 :
        lim = length // 2 - 1
    else :
        lim = length // 2

    # Checking if the number is palindromic
    palindromic = True
    i = 0
    while i <= lim :
        if numList[i] != numList[length-1-i] :
            palindromic = False
        i = i+1

    return palindromic


def problem36() :

    i = 0
    sum = 0
    while i < 1000000 :
        if checkPalindromic(i):
            temp = binaryMaker(i)
            if checkPalindromic(temp) :
                sum = sum + i
        i = i + 1

    print(sum)

problem36()







