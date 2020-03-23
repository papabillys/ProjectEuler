# Problem 19 - Counting Sundays
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June and November.
# All the rest have thirty-one,
# Saving February alone, which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000) ?
#
# Answer: 171

def checkLeapYear(year):

    if year%4 != 0 :
        return False
    yearIsLeap = True
    if year%100 == 0 :
        if year%400 != 0 :
            yearIsLeap = False
    return yearIsLeap

def daysOfMonth(month, year):

    if month==2 :
        if checkLeapYear(year):
            days = 29
        else :
            days = 28
        return days

    if month==4 or month==6 or month==9 or month==11 :
        days = 30
    else :
        days = 31
    return days


def checkYear(weekday, year):

    sunday_counter = 0
    month = 1
    while month <= 12:
        day = 1
        weekday = weekday+1
        if weekday == 8:
            weekday = 1
        if weekday == 7:
            sunday_counter = sunday_counter+1
        days_of_month = daysOfMonth(month, year)
        while day <= days_of_month:
            day = day+1
            weekday = weekday+1
            if weekday == 8:
                weekday = 1
        month = month+1
    if year == 1900:
        sunday_counter = 0

    return sunday_counter, weekday


def problem19():
    year = 1900
    weekday = 0
    counter = 0
    while year < 2001:
        [sundays, weekday] = checkYear(weekday, year)
        counter = counter + sundays
        year = year+1

    print(counter)


problem19()