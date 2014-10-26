# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = yearsInDays(year1, year2, month1, month2) + monthsInDays(month1, month2) + daysInDays(day1, day2)
    return days

#if the years are the same and month1 == 1 and month 2 > 2

def yearsInDays(year1, year2, month1, month2):
    diffInYears = year2 - year1
    numOfLeap = 0
    if isLeap(year1) and year1 == year2 and month1 == 1 and month2 > 2:
        numOfLeap = 1
    elif year1 != year2:
        if isLeap(year1) and month1 == 1:
            numOfLeap = 1
        if isLeap(year2) and month2 > 2:
            numOfLeap = numOfLeap + 1
    start = year1 + 1
    while start < year2:
        if isLeap(start):
            numOfLeap = numOfLeap + 1
        start = start + 1
    return diffInYears * 365 + numOfLeap

def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

#Can use logic, but it's not really worth the confusion of needing to understand it. There is a small finite set of possibilities,
#and it's just easier to hard code the possible months.
def daysInMonth(month):
    if month == 2:
        return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    return 30

def monthsInDays(month1, month2):
    if month1 < month2:
        start = month1
        end = month2
        direction = 1
    else:
        start = month2
        end = month1
        direction = -1
    monthInDays = 0
    while start < end:
        monthInDays = monthInDays + daysInMonth(start)
        start = start + 1
    return monthInDays * direction

def daysInDays(day1, day2):
    return day2 - day1




daysBetweenDates(2012,1,1,2012,2,28)
daysBetweenDates(2012,6,29,2013,6,29)
daysBetweenDates(2011,6,30,2012,6,30)
daysBetweenDates(1900,1,1,1999,12,31)


#Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
