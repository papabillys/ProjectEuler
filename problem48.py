# Problem 48 -
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
#
# Answer: 9110846700

def problem48():

    i = 1
    sum = 0
    while i<= 1000 :
        temp = pow(i,i)
        sum = sum+temp
        i = i+1
    divNum = pow(10,10)
    print(sum%divNum)


problem48()