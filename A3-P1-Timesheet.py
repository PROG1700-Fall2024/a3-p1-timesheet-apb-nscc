#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     W0487099
#Student Name:  Alex Barr

"""
For this assignment, I tried to put everything into functions and then use those functions as pseudo-code. I used a "try/except" statement I learned
from a youtube short, it may be a bit janky; I'm still not 100% how to use it and I probably overcoded it, but it works so I'm going to leave it for now.
"""

#This function determines that only correct values can be inputted by the user
def corrector(_minValue: int, _maxValue: int, _input: str, _errorMessage: str, _day):
    ### TRYING TRY/EXCEPT CODE I FOUND ON A YOUTUBE SHORT
    while True:
        try:
            if int(_input) < _minValue or int(_input) > _maxValue:
                print(_errorMessage)
                return corrector(_minValue, _maxValue, (input(f"Enter hours worked on Day #{_day + 1}: ")), _errorMessage, _day)
            else:
                return int(_input)
        except ValueError:
            print(_errorMessage)
            return corrector(_minValue, _maxValue, (input(f"Enter hours worked on Day #{_day + 1}: ")), _errorMessage, _day)

#This function is part of the next function and it appends user information to a list; In this case hours worked to a list of days worked
def dayHoursWorked(_day, _list):
    _list.append(corrector(1,24,(input(f"Enter hours worked on Day #{_day + 1}: ")),"Value Invalid. Try Again.",_day))

#This function prompts the user to input amount of hours worked per day, for as many days are in the workDays variable
def EnterHoursWorked(_daysWorked: list, _daysWithMaxHours: list, _indexMaxHours: list, _workDays: int):
    for i in range(_workDays):
        dayHoursWorked(i, _daysWorked)

    for i in range(len(_daysWorked)):
        if _daysWorked[i] == max(_daysWorked):
            _daysWithMaxHours.append(max(_daysWorked))
            _indexMaxHours.append(i)

#This takes information we have already received, typecasts it into either ints or floats, gets the max hours worked, gets the total numbers worked
#and gets the average hours worked. Normally this would be done in three functions but I decided to try out multiple returns.
def CalculateHoursWorked(_daysWorked, _workDays):
    _maxHoursWorked = int(max(_daysWorked))
    _totalHoursWorked = int(sum(_daysWorked))
    _averageHoursWorked = float(_totalHoursWorked / _workDays)
    return _maxHoursWorked, _totalHoursWorked, _averageHoursWorked

#This just executes code that tells the user relevant information such as total hours worked per week, average hours per week worked and the days
#with the most hours worked. It presenting information that we viewing the code already have information on, but this code presents it to the user.
def ShowProductiveDaysAndAverage(_daysWithMaxHours, _indexMaxHours, _averageHoursWorked, _totalHoursWorked, _dividerLength):
    print("-"*_dividerLength)
    print("The most hours worked on:")
    for i in range(len(_daysWithMaxHours)):
        print(f"Day #{_indexMaxHours[i] + 1} when you worked {_daysWithMaxHours[i]} hours.")
    print("-"*_dividerLength)

    print(f"The total number of hours worked was: {_totalHoursWorked}")
    print(f"The average number of hours worked each day was: {_averageHoursWorked}")
    print("-"*_dividerLength)

#This code shows the days worked that are under 7 hours IF there are any days under 7 hours worked. Otherwise it doesn't show anything.
def ShowSlackOffDays(_daysWorked, _minShouldWork, _workDays):
    if min(_daysWorked) < 7:
        print("Days you slacked off (i.e. worked less than 7 hours):")
        for i in range(_workDays):
            if _daysWorked[i] < _minShouldWork:
                print(f"Day #{_daysWorked.index(_daysWorked[i]) + 1}: {_daysWorked[i]} hours ")
 
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    
    #Local Variable Initialization
    daysWorked = []
    daysWithMaxHours = []
    indexMaxHours = []
    maxHoursWorked = 0.0
    totalHoursWorked = 0.0
    averageHoursWorked = 0.0
    workDays = 5
    minShouldWork = 7
    dividerLength = 60

    EnterHoursWorked(daysWorked,daysWithMaxHours,indexMaxHours,workDays)
    
    #Calculate hours worked and place them in variables
    maxHoursWorked, totalHoursWorked, averageHoursWorked = CalculateHoursWorked(daysWorked, workDays) # I looked up how to get multiple values on stack overflow
    
    ShowProductiveDaysAndAverage(daysWithMaxHours, indexMaxHours, averageHoursWorked, totalHoursWorked, dividerLength)
    
    ShowSlackOffDays(daysWorked, minShouldWork, workDays)

    print("")

    # YOUR CODE ENDS HERE

main()