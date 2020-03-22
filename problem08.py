# Problem 8 - 	Largest product in a series
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
#
# Answer: 23514624000
# The 1000digits number is saved in a txt file with name problem8_input

def problem8():

    file = open("problem8_input", "r")
    number_str = ""
    for x in file:
        number_str = number_str + x.strip()

    # If a number is 0 , product is 0
    # I will delete 12 digits before and after 0 digit

    number_strList = number_str.rsplit("0")
    i = 0
    number_strList_new = []
    for x in number_strList :
        if len(x) >= 13 :
            number_strList_new.append(x)
        i = i+1

    maxProduct = 0
    for x in number_strList_new :
        start = 0
        while len(x) - start >= 13 :
            product = 1
            i = start
            while i-start <= 12 :
                product = product * int(x[i])
                i = i+1
            if product > maxProduct :
                maxProduct = product

            start = start+1

    print( maxProduct )


problem8()
