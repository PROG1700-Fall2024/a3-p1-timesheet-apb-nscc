#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     W0487099
#Student Name:  Alex Barr

daysWorked = []
daysWithMaxHours = []
indexMaxHours = []
maxHoursWorked = 0.0
totalHoursWorked = 0.0
averageHoursWorked = 0.0
workDays = 5
minShouldWork = 7

dividerLength = 60

def corrector(_minValue: int, _maxValue: int, _input: str, _errorMessage: str, _day):
    if int(_input) < _minValue or int(_input) > _maxValue:
        print(_errorMessage)
        return corrector(_minValue, _maxValue, int(input(f"Enter hours worked on Day #{_day + 1}: ")), _errorMessage, _day)
    else:
        return _input

def dayHoursWorked(_day, _list):
    _list.append(corrector(1,23,int(input(f"Enter hours worked on Day #{_day + 1}: ")),"That Number is Out of Range. Try Again.",_day))

def EnterHoursWorked(_daysWorked: list, _daysWithMaxHours: list, _indexMaxHours: list, _workDays: int):
    for i in range(_workDays):
        dayHoursWorked(i, _daysWorked)

    for i in range(len(_daysWorked)):
        if daysWorked[i] == max(_daysWorked):
            daysWithMaxHours.append(max(_daysWorked))
            _indexMaxHours.append(i)

def CalculateHoursWorked(_maxHoursWorked, _totalHoursWorked, _averageHoursWorked, _daysWorked, _workDays):
    _maxHoursWorked = int(max(_daysWorked))
    _totalHoursWorked = int(sum(_daysWorked))
    _averageHoursWorked = float(_totalHoursWorked / _workDays)


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    EnterHoursWorked(daysWorked,daysWithMaxHours,indexMaxHours,workDays)
    CalculateHoursWorked(maxHoursWorked, totalHoursWorked, averageHoursWorked, daysWorked, workDays)


    print("-"*dividerLength)
    print("The most hours worked on:")
    for i in range(len(daysWithMaxHours)):
        print(f"Day #{indexMaxHours[i] + 1} when you worked {daysWithMaxHours[i]} hours.")
    print("-"*dividerLength)

    print(f"The total number of hours worked was: {totalHoursWorked}")
    print(f"The average number of hours worked each day was: {averageHoursWorked}")
    print("-"*dividerLength)

    print("Days you slacked off (i.e. worked less than 7 hours):")

    for i in range(workDays):
        if daysWorked[i] < minShouldWork:
            print(f"Day #{daysWorked.index(daysWorked[i]) + 1}: {daysWorked[i]} hours ")

    # YOUR CODE ENDS HERE

main()