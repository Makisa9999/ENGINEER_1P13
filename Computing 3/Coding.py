def intAccept(x):
    x = x + 1
    return x

a = 1

def globalVar():
    global a
    a += 1
    return a

print(intAccept(1))
print(globalVar())
