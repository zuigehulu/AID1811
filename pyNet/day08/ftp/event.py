from threading import Event

#创建事件对象
e = Event()

e.set()

e.wait()

print("**************************")
e.clear()
e.wait()

print("-------------------------")
##