def mymax(a,*args):
    if len(args)==0:
        return max(a)
    elif len(args) > 0:
        return max(a,*args)
    
    