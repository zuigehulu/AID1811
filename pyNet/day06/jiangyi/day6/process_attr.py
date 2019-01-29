from multiprocessing import Process 
from time import ctime,sleep 

def tm():
    for i in range(4):
        sleep(2)
        print(ctime())

p = Process(target = tm,name = "Tarena")

p.daemon = True  #必须在start前使用

p.start()

print("Process name:",p.name)
print("Process PID:",p.pid)
print("Process alive:",p.is_alive())

# p.join()



