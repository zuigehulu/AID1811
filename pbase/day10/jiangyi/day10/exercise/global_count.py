# 练习:
#   用全局变量记录一个函数hello 被调用的次数,部分代码如下:
#     count = 0
#     def hello(name):
#         print('你好')
#         ...  # 此处自己完善
    
#     hello('小张')
#     while True:
#         s = input('请输入姓名: ')
#         if not s:
#             break
#         hello(s)
#     print("hello函数调用的次数是", count)


count = 0
def hello(name):
    print('你好', name)
    global count
    count += 1

hello('小张')
while True:
    s = input('请输入姓名: ')
    if not s:
        break
    hello(s)
print("hello函数调用的次数是", count)
