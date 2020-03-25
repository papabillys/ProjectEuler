# Problem 52 - Permuted multiples
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
#
# Answer: 142857

def sameDigits(num1, num2):
    num1_list = list(str(num1))
    num2_list = list(str(num2))
    for x in num1_list:
        if str(x) not in num2_list:
            return False
    for y in num2_list:
        if str(y) not in num1_list:
            return False
    return True


def problem52():
    flagExit = False
    i = 1
    while not flagExit:
        if sameDigits(i,2*i) and sameDigits(i,3*i) and sameDigits(i,4*i) and sameDigits(i,5*i) and sameDigits(i,6*i):
            flagExit = True
        i = i+1

    # Answer
    print(i-1)


problem52()