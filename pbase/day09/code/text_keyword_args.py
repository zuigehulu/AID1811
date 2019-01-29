def mymax(arg1,arg2,*args):
    y = 0
    if type(arg1) is not int:
        for x in arg1:
            if y < x:
                y = x 
    elif type(arg2) is not int:
            for x in arg1:
                if y < x:
                    y = x 
    else:
        y = arg1 
        if y < arg2:
            y = arg2
        for x in args:
            if y < x:
                y = x 
    return y

print(mymax([6,8,5,3]))
print(mymax((100,200)))
print(mymax(1,2,5,9,7))
print(mymax())
