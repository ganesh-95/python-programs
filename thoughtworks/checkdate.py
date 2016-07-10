
#check whether date is valid or not

import datetime

def valid_date(year, month, day):
    correct_date = None
    try:
        new_date = datetime.datetime(year, month, day)
        correct_date = True
    except ValueError:
        correct_date = False
    return correct_date


print str(valid_date(year=input('year:'), month=input('month:'), day=input('day:')))

    
