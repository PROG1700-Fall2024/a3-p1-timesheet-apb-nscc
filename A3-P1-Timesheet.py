#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     W0487099
#Student Name:  Alex Barr

daysWorked = []
maxHoursWorked = 0.0
totalHoursWorked = 0.0
averageHoursWorked = 0.0
workDays = 5
minShouldWork = 7

dividerLength = 60

def dayHoursWorked(_day):
    daysWorked.append(int(input(f"Enter hours worked on Day #{_day + 1}: ")))

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    for i in range(workDays):
        _hours = dayHoursWorked(i)

        
    maxHoursWorked = int(max(daysWorked))
    totalHoursWorked = int(sum(daysWorked))
    averageHoursWorked = float(totalHoursWorked / workDays)

    print("-"*dividerLength)
    print("The most hours worked on:")
    print(f"Day #{daysWorked.index(maxHoursWorked) + 1} when you worked {maxHoursWorked}.")
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