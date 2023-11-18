def drop_off(color):
    arm.activate_autoclaves()
    left_Potentiometer = potentiometer.left()
    if left_Potentiometer > 50 and left_Potentiometer < 100:
        # Run function for moving the arm to the top of the box and releasing. 
        arm_top()
        arm.deactivate_autoclaves()
        arm.home()
        return 1
    elif left_Potentiometer == 100: 
        arm.open_autoclave(color)
        time.sleep(5)
        # Run a function to move the arm to the bottom drawer and releasing. 
        arm_drawer()
        arm.open_autoclave(color, False)
        time.sleep(5)
        arm.deactivate_autoclaves()
        arm.home()
        return 2
    arm.deactivate_autoclaves()
    arm.home()
    return 0

def arm_top():
    arm.rotate_elbow(-30)
    arm.rotate_shoulder(40)
    arm.control_gripper(-45)
    return 0

def arm_drawer():
    arm.rotate_elbow(30)
    arm.rotate_shoulder(20)
    arm.control_gripper(-45)
    time.sleep(2)
    arm.rotate_shoulder(-20)
    arm.rotate_elbow(-30)
    time.sleep(2)
    return 0