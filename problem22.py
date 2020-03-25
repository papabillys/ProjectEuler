# Problem 22 - Names scores
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?
#
# Answer: 871198282
# The names.txt file is renamed as problem22_input.txt

def problem22():

    # Get a list of all the names sorted and without " or , symbols
    file = open("problem22_input.txt", "r")
    names = file.readline()
    names = names.rsplit(",")
    nameList = []
    for x in names:
        temp = x.replace("\"", " ")
        nameList.append(temp.strip())
    nameList.sort()

    # Calculate total score of all the names
    pos = 1
    total = 0
    for name in nameList:
        name_char_list = list(name)
        name_value = 0
        for x in name_char_list:
            value = ord(x) - 64
            name_value = name_value + value
        total = total + name_value * pos
        pos = pos + 1

    print(total)

problem22()