import random, math

# Variables
g = 9.81
theta = random.random() * 45
theta_rads = math.radians(theta)
d = float(input("Please enter the distance to our target zombie: "))
v = math.sqrt((g*d)/(math.sin(2*theta_rads)))

# Output
print("---------------------------------------------------")
print("Ready for launch!")
print("Set angle to ", theta, "degrees.")
print("Set speed to ", v, "m/s.")
print("---------------------------------------------------")

"""
1. The program requires that the distance entered by the 
user follows syntactically correct floating-point
values greater than 0. What will happen in the following
scenarios and why?
    - The user enters a negative value. 
        The program would give us a math domain error 
        since we would try to find the square root of 
        a negative value. In math we call these imaginary 
        values.
    - The user enters non numeric characters.
        The program would give us a value error since we 
        would try to convert a non float input into a float
2. Would the behaviour of your program change if the line 
g = 9.81 was defined after you calculated the value for V? 
Justify your answer. (Hint: You may need to go to Kernel > 
Restart & Clear Output before trying this.)
    Yes, the program would not work at all. This is because
    when the program is trying to figure out the value for
    V it needs a variable called g in order to get that 
    value. However since the variable is defined after its 
    use and the compiler runs code one line at a time, it 
    would not know the value that it should use for g. 
"""