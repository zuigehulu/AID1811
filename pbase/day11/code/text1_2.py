L = [[3,5,8],10,[[13,14],15,18],20]

def print_list(lst):
    sum = 0
    for x in lst:
        if type(x) is not int:
            sum += print_list(x)
        else:
            sum += x
    return sum
sum = print_list(L)
print(sum)

