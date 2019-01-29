from threading import Thread,Event
from time import sleep

s = None
e =Event()

def bar():
    print("Bar 拜山头")
    sleep(1)
    global s
    s = '天王盖地虎'
    e.set()
b = Thread(target=bar)

b.start()

print("说对口令就是自己人")

e.wait()#阻塞等待分支线程set
if s == '天王盖地虎':
    print("确认过眼神，你是对的人")
else:
    print("打死他")
e.clear()
e.wait()
print('asdf')
b.join()    