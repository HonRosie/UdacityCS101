def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    return


###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextday(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):

    newDay, newMonth, newYear = 0,0,0
    if day == 30:
        newDay = 1
    else:
        newDay += day + 1

    if newDay == 1:
        if month != 12:
            newMonth = month + 1
        else:
            newMonth = 1
    else:
        newMonth = month

    if newMonth == 1:
        newYear = year + 1
    else:
        newYear = year

    # YOUR CODE HERE
    return newYear, newMonth, newDay


print nextDay(1999, 12, 30)
print nextDay(2013, 1, 30)
print nextDay(2012, 12, 30)
print nextDay(2012, 1, 1)
