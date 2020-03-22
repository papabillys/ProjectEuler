# Problem 13 - Large sum
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#
# Answer: 5537376230
# The 1000 50-digit numbers are saved in a txt file with name problem13_input

def problem13():

    file = open("problem13_input", "r")
    number = 0
    for x in file:
        number = number + int(x.strip())

    number_str = str(number)
    first_digits = number_str[0:10]

    print(first_digits)


problem13()