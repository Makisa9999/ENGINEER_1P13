# %% [markdown]
# # Computing 1B Assignment

# %% [markdown]
# ---
# ## Background
# 
# Your task is to write a program for a system that will determine the speed at which to fire a projectile at enemy zombies. Lucky for us, our system is equipped with a proximity sensor that displays the distance from our projectile launcher to the nearest zombie. 
# 
# Your program will:
# 
# 1.   Ask the user for the distance to the nearest zombie.
# 2.   Display the angle and velocity required to set the projectile launcher in order to hit the zombie.
# 
# ![Figure 1](data:image/png;base64,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)
# 
# Fortunately for us, these zombies are extremely slow, and we can treat this scenario as a simple projectile motion problem. After some clever manipulation of the kinematic equations, we can derive a formula used to calculate the velocity **V** to fire our projectile in order to travel distance **d** in the horizontal direction at a given angle **theta** (in radians). This equation is given below:
# 
# <br/>
# \begin{align}
#   V = \sqrt{\frac{g*d}{sin(2*thetaRads)}} \tag{1}
# \end{align}
# <br/>
# 
# The constant **g** is the acceleration due to gravity on Earth ($9.81 m/s^2 $). It is also notable that the projectile launcher is confined to fire at an angle *0 ≤ theta < 45* in degrees. For simplicity, we assume that all units are SI units.
# 
# 
# 

# %% [markdown]
# ---
# ## Requirements
# 
# Write a computer program for a system that will determine the speed at which to fire a projectile. The user will be asked to enter the distance to the nearest zombie and the system will determine the angle and velocity to set the projectile launcher. The requirements of the program are given below. Each step should be implemented in the respective order that they are listed:
# 
# 
# 1. The program defines the variable **g** = 9.81 
# <br/><br/>
# 2. The program defines the variable **theta**, representing the angle theta in degrees. **theta** is calculated by randomly generating a number between 0 and 1, and multipying this number by 45. (Notice that the angle conforms to the requirement: *0 ≤ theta < 45*)
# <br/><br/>
# 3. The program defines the variable **theta_rads** as the angle from the previous step in radians. (*Hint: There is a shortcut to convert from degrees to radians using the math module*)
# <br/><br/>
# 4. The program defines the variable **d**. The value of **d** is found by prompting the user to input the distance to the zombie with the message: 
#   >*“Please enter the distance to our target zombie: ”* <br/> 
#   
#    Ensure that the value stored to the variable **d** is a float. 
# <br/>
# 5. The program defines the variable **V**. The value of **V** is calculated with the projectile equation (1), using the values for **g**, **d**, and **theta_rads**.
# <br/>
# \begin{align}
#   V = \sqrt{\frac{g*d}{sin(2*thetaRads)}} \tag{1}
# \end{align}
# <br/>
# 6. Once **V** is calculated, the program prints the following messages on seperate lines: 
# 
#    >*Ready for launch!, Set angle to &lt;angle value&gt; degrees, Set speed to &lt;velocity&gt; m/s* <br/>
# 
#    Where *&lt;angle&gt;* and *&lt;velocity&gt;* are the actual values for **theta** and **V**, respectively. An example output is shown below:
# 
#    >*Ready for launch!<br/>
#    >Set angle to 42.2325353123 degrees<br/>
#    >Set speed to 400.00 m/s<br/>*
# 7. Your program must have valid python 3 syntax and run without errors. Please ensure your program can run before you submit!
# 

# %% [markdown]
# ---
# ## Implementation
# 
# Please use the following cell to write your code.

# %%
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

# %% [markdown]
# ---
# ## Reflective Questions
# 
# 1. The program requires that the distance entered by the user follows syntactically correct floating-point values greater than 0. What will happen in the following scenarios and why?
#     * The user enters a negative value.
#     * The user enters non numeric characters.
# 
# 2. Would the behaviour of your program change if the line g = 9.81 was defined *after* you calculated the value for V? Justify your answer. (Hint: You may need to go to Kernel > Restart & Clear Output before trying this.)
# 
# Please answer all questions in the cell below!

# %% [markdown]
# ```
# DOUBLE CLICK TO EDIT THIS CELL. DO NOT DELETE QUOTATION MARKS
# 1. The program requires that the distance entered by the 
# user follows syntactically correct floating-point
# values greater than 0. What will happen in the following
# scenarios and why?
#     - The user enters a negative value. 
#         The program would give us a math domain error 
#         since we would try to find the square root of 
#         a negative value. In math we call these imaginary 
#         values.
#     - The user enters non numeric characters.
#         The program would give us a value error since we 
#         would try to convert a non float input into a float
# 2. Would the behaviour of your program change if the line 
# g = 9.81 was defined after you calculated the value for V? 
# Justify your answer. (Hint: You may need to go to Kernel > 
# Restart & Clear Output before trying this.)
#     Yes, the program would not work at all. This is because
#     when the program is trying to figure out the value for
#     V it needs a variable called g in order to get that 
#     value. However since the variable is defined after its 
#     use and the compiler runs code one line at a time, it 
#     would not know the value that it should use for g. 
# 
# ```

# %% [markdown]
# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 1b dropbox on avenue with the naming convention: macID_CL1b.py
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely receive zero.**
# 
# This assignment is due the day of your Lab section at 11:59 PM EST
# 
# Late labs will not be accepted


