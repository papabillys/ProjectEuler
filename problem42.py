# Problem 42 - Coded triangle numbers
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?
#
# Answer: 162
# The words.txt file is renamed as problem42_input.txt

def getNameScores(name):

    file = open(name, "r")
    words = file.readline()
    words = words.rsplit(",")
    words_score_list = []
    max_sum = 0
    for x in words:
        temp = x.replace("\"", " ")
        temp = temp.strip()
        word_list = list(temp)
        sum = 0
        for y in word_list:
            value = ord(y)-64
            sum = sum + value
        if sum > max_sum:
            max_sum = sum
        words_score_list.append(sum)

    return words_score_list,max_sum

def getTriangleNumbers(limit):

    exitFlag = False
    triangleList = []
    i = 1
    while not exitFlag:
        t = 0.5 * i * (i+1)
        t = int(t)
        triangleList.append(t)
        if t > limit:
            exitFlag = True
        i = i+1
    return triangleList


def problem42():

    # Get scores of the words and max score ( need max score to set the limit in finding triangle numbers )
    file_name = "problem42_input.txt"
    [words_scores,max_score] = getNameScores(file_name)

    # Get triangle numbers
    triangle_list = getTriangleNumbers(max_score)

    # Count triangle words
    counter = 0
    for x in words_scores:
        if x in triangle_list:
            counter = counter+1

    print(counter)


problem42()
