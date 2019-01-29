def mymax(a,*args):
    if len(args) == 1:
        iterable = args[0]
        zuida = iterable[0]
        for x in iterable:
            if zuida < x:
                zuida = x
        return zuida
    elif len(args) >1 :
        zuida = args[0]
        for x in args:
            if zuida < x:
                zuida = x
        return zuida

print(mymax([6,8,5,3]))
print(mymax((100,200)))
print(mymax(1,2,5,9,7))