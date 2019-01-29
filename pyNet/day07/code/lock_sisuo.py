from threading import Thread,Lock,RLock
import time

mutexA=Lock()
mutexB=Lock()

class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到了A1锁' %self.name)

        mutexB.acquire()
        print('%s 拿到了B1锁' %self.name)
        # time.sleep(0.1)
        mutexB.release()
        print("B锁释放")
        print("1234")
        mutexA.release()
        print("A锁释放")


    def f2(self):
        mutexB.acquire()
        print('%s 拿到了B2锁' %self.name)
        time.sleep(0.1)

        mutexA.acquire()
        print('%s 拿到了A2锁' %self.name)
        mutexA.release()
        print("A锁释放")

        mutexB.release()
        print("B锁释放")



if __name__ == '__main__':
    for i in range(10):
        t=MyThread()
        t.start()

    print('主')

# 死锁