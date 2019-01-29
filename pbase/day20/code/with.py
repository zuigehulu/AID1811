fr = open('./test.txt','r')
# with open('test.txt','r') as fr:
with fr:
    for line in fr:
        print(line)
#with　语句执行完的时候fr就会被自动关闭
