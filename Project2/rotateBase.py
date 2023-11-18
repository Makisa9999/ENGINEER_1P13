arm.home()
def rotate_base(color):
    
    color='green'    
    b = potentiometer.right()
    while arm.check_autoclave(color) == False:
        a = potentiometer.right()
        c = a-b
        b = a
        arm.rotate_base(c*348)


    return ()

rotate_base()