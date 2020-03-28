# Problem 74 - Digit factorial chains
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
# it turns out that there are only three such loops that exist:
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
# Starting with 69 produces a chain of five non-repeating terms,
# but the longest non-repeating chain with a starting number below one million is sixty terms.
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
#
# Answer: 402


import math


# This function returns the sum of the factorial of the digits of the number given as parameter.
def get_sum_of_factorials(number):
    num_str_list = list(str(number))
    sum = 0
    for number in num_str_list:
        sum = sum + math.factorial(int(number))
    return sum


# This function finds the chain of the number given as parameter.
# If this chain contains sixty numbers, then the function returns True, else returns False.
def get_sixty_streak_number(number):
    chain = []
    exit_flag = False
    chain.append(number)
    while not exit_flag:
        temp = get_sum_of_factorials(chain[len(chain)-1])
        if temp not in chain:
            chain.append(temp)
        else:
            exit_flag = True
    if len(chain) == 60:
        return True
    else:
        return False


def problem74():
    # Starting number is 3 because 1! = 1 and 2! = 2
    i = 3
    counter = 0
    while i < 1000000:
        if get_sixty_streak_number(i):
            counter = counter+1
        i = i+1
        print(i)


problem74()