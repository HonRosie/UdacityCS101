# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.



#days = 0
#while date1 is before date2
#	date1 = advance to next day
#	days += 1


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(month, year):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def daysInMonth(month, year):
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        return 31
    if (month == 4) or (month == 6) or (month == 9) or (month == 11):
        return 30
    if (month == 2):
        if isLeapYear(year):
            return 29
        else:
            return 28

def isLeapYear(year):
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 == 0:
        return True
    else:
        return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    days = 0
    while isBeforeDate1(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1

    # YOUR CODE HERE!
    return days


def isBeforeDate1(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    else:
        if month1 < month2:
            return True
        if day1 < day2:
            return True
        else:
            return False



#print daysBetweenDates(2011,6,30,2012,6,30)
#print daysBetweenDates(2011,1,1,2012,8,8)
#print daysBetweenDates(1900,1,1,1999,12,31)
#print daysBetweenDates(2012,5,30,2013,3,15)
#daysBetweenDates(2012,1,1,2012,2,28)
#daysBetweenDates(2012,1,1,2012,1,31)

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
