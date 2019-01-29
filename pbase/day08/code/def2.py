g = 10    #全局变量
def say_hello(hello):
    value = 100   #局部变量
    print("hello world")
    print("hello china")
    print("value=",value)
    print("g=",g)
    # g = 20
    # print('g=',g)
    return [1,2,3,4,5]

d=say_hello(g)
print(d)
