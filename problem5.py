# Problem 5 - Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# Answer: 232792560

def problem5():

    temp = 1
    exitFlag = False
    while not exitFlag:
        i = 1
        exitFlag2 = False
        while i <= 20 and not exitFlag2 :
            if temp%i != 0 :
                exitFlag2 = True
            i = i+1
        if exitFlag2 :
            temp = temp+1
        else :
            exitFlag = True

    print("Number is ", temp)


problem5()