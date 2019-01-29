def my_yunsuan(*args,yunsuan):
    if yunsuan == '+':
        return sum(args)
    elif yunsuan == '-':
        jian = args[0]    
        for x in args:
            jian -= x
        return jian
    elif yunsuan == '*':
        cheng = 1
        for x in args:
            cheng *= x
        return cheng
    elif yunsuan == '/':
        chu = args[0]
        for x in args:
            chu /= x
        return chu

print(my_yunsuan(1,2,3,4,5,6,yunsuan = '+'))
print(my_yunsuan(1,2,3,4,5,6,yunsuan = '-'))
print(my_yunsuan(1,2,3,4,5,6,yunsuan = '/'))
print(my_yunsuan(1,2,3,4,5,6,yunsuan = '*'))



