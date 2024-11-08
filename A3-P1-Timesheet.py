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

def dayHoursWorked(_day):
    daysWorked.append(int(input(f"Enter hours worked on Day #{_day + 1}: ")))

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    for i in range(workDays):
        dayHoursWorked(i)

    for i in range(len(daysWorked)):
        if daysWorked[i] == max(daysWorked):
            daysWithMaxHours.append(max(daysWorked))
            indexMaxHours.append(i)
        
    maxHoursWorked = int(max(daysWorked))
    totalHoursWorked = int(sum(daysWorked))
    averageHoursWorked = float(totalHoursWorked / workDays)

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