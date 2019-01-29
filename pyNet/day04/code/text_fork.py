from os import fork
fk = fork()
if fk > 0:
    print('第一行')
elif fk == 0:
    print('第二行')
elif fk < 0:
    print('第三行')

print('结束')