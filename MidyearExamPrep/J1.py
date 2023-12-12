bigBox = int(input("How many big boxes"))
smallBox = int(input("How many small boxes"))

def cupcakesLeftOver(bigBox, smallBox):
    numStudents = 28
    return (bigBox * 8 + smallBox * 3) - 28

print(cupcakesLeftOver(bigBox, smallBox))