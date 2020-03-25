# Problem 34 - Digit factorials
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
# Answer: 40730

# 9! has the largest result which is 362880 .
# 999999 ( 6-digit ) -> 2177280 and 2177280 < 999999 .
# 9999999 ( 7-digit ) -> 2540160  and 2540160 > 9999999 .
# So upper limit = 9999999 and starting number = 3 because 1! and 2! are not included in the sum

def curiousNumber(number):
    number_str = str(number)
    number_str = list(number_str)
    sum = 0
    for x in number_str:
        temp = int(x)
        i = 1
        num = 1
        while i <= temp:
            num = num*i
            i = i+1
        sum = sum+num

    if sum == number:
        return True
    else:
        return False

def problem34():
    upper_limit = 9999999
    i = 3
    sum = 0
    while i < upper_limit:
        if curiousNumber(i):
            sum = sum+i
        i = i+1
        print(i)
    print(sum)


problem34()
