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

def averageGrade1(grade1, grade2, grade3, grade4, grade5):
    sum = 0
    sum = grade1 + grade2 + grade3 + grade4 + grade5
    average = sum / 5
    return average

print(averageGrade1(95,96,97,98,99))

