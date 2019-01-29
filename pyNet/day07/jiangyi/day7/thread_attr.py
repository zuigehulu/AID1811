from threading import Thread,currentThread 
from time import sleep 

def fun():
    print("当前线程:",currentThread().getName())
    sleep(3)
    print("线程属性示例")

#创建线程对象
t = Thread(target=fun,name="Tedu")

#设置daemon
t.setDaemon(True)
print("Daemon:",t.isDaemon())

t.start()

#线程名称
t.setName("tarena")
# print("name:",t.name)
print("name:",t.getName())

#线程状态
print("Is alive:",t.is_alive())

# t.join()
