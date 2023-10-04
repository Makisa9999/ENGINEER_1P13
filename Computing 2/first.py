def averageGrade():
    listOfGrades = []
    sum = 0
    numGrades = int(input("How many grades are you willing to input: "))
    for i in range(numGrades):
        currentGrade = float(input("Enter you grade: "))
        listOfGrades.append(currentGrade)
        sum = sum + currentGrade
    average = sum / numGrades
    return average

print(averageGrade())