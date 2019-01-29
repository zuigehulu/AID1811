count = 0
def hello(name):
    print('你好')
    global count
    count += 1

   
hello('小张')
while True:
    s = input("请输入姓名")
    if not s:
        break
    hello(s)
print("hello函数调用的次数是:",count)