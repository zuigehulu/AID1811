v = 100
def f1():
   global v  #声明v为全局变量
   v = 200    #改变v的值

f1()
print("v=",v)