arm = 1.59
checkAutoclave = True
import math

if (checkAutoclave == True) and ((arm == round(91*math.pi/180,2)) or (arm == round(-91*math.pi/180,2))):
    print(True)
print(False)
