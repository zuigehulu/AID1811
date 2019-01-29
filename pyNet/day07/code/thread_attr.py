from threading import Thread,currentThread
from time import sleep

#线程函数
def fun():
    print("当前线程对象:",currentThread().getName())
    sleep(3)
    print("线程属性示例")
#创建线程对象
t = Thread(target=fun,name='Tedu')
#设置daemon
t.setDaemon(True)
print("Daemon:",t.isDaemon())

t.start()
t.setName("tarena")

#线程名称
print("name:",t.getName())

#线程状态
print("is alive:",t.is_alive())
# t.join()
