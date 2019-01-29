try:
    myfile = open("pbase/day16/code/info.txt")
    L = myfile.readlines()
    myfile.close()
except OSError:
    print('打印失败')
# print(L)
for x in L:
    if x == '\n':
        print()
    else:
        print(x,end = " ")
print()
