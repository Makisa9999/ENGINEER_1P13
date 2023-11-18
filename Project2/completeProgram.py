import random

# Random List of Numbers 1-6
def randomList():
    lst = [1,2,3,4,5,6]
    # It is randomly going to shuffle the above list giving us random numbers from 1-6 without repeating
    random.shuffle(lst)
    return lst

# Rotate base function
def rotate_base(color):
    color='green' # delete this when running the program since this will only work when green is the color
    b = potentiometer.right()
    while arm.check_autoclave(color) == False:
        a = potentiometer.right()
        c = a-b
        b = a
        arm.rotate_base(c*348)
    return ()

def drop_off(color):
    arm.activate_autoclaves()
    left_Potentiometer = potentiometer.left()
    if left_Potentiometer > 50 and left_Potentiometer < 100:
        # Run function for moving the arm to the top of the box and releasing. 
        arm.deactivate_autoclaves()
        arm.home()
        return 1
    elif left_Potentiometer == 100: 
        arm.open_autoclave(color)
        time.sleep(5)
        # Run a function to move the arm to the bottom drawer and releasing. 
        arm.open_autoclave(color, False)
        time.sleep(5)
        arm.deactivate_autoclaves()
        arm.home()
        return 2
    arm.deactivate_autoclaves()
    arm.home()
    return 0

# Variables
container = {
    1:{"color":"red", "size":"small"}, 
    2:{"color":"green", "size":"small"}, 
    3:{"color":"blue", "size":"small"}, 
    4:{"color":"red", "size":"big"}, 
    5:{"color":"green", "size":"big"}, 
    6:{"color":"blue", "size":"big"}
}

# arm.home()
randomSequence = randomList()
for i in range(0,len(randomSequence),1):
    color = container[randomSequence[i]]["color"]
    size = container[randomSequence[i]]["size"]
    # pick_up()
    # close_gripper()
    # home_position()
    # rotate_base(color)
    # drop_off(color)
    

