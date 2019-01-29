import time,os,random
from multiprocessing import Queue,Process,JoinableQueue

def procducer(food,q):  #定义一个生产者函数
    for i in range(1,4):
        res = "%s%s" %(food,i)
        time.sleep(0.5)
        q.put(res)   #往框里面放一个包子
        print('%s 生产了 %s %s'%(os.getpid(),res,time.ctime()))
    q.join()   #不生产了，等东西被取完,等消费者发消息

def consumer(q):  #定义一个消费者函数
    while True:
        res = q.get()
        # if res is None:
        #     break
        print('\033[43;1m%s 吃了%s\033[0m %s'%(os.getpid(),res,time.ctime()))
        time.sleep(random.randint(1,2))
        q.task_done()   #发信号的操作

if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=procducer,args=('包子',q,))
    p2 = Process(target=procducer,args=('玉米',q,))
    p3 = Process(target=procducer,args=('狗粮',q,))

    c1 = Process(target=consumer,args=(q,))
    c2 = Process(target=consumer,args=(q,))
    c1.daemon=True
    c2.daemon=True
    p1.start()
    p2.start()
    p3.start()

    c1.start()
    c2.start()
    p1.join()
    p2.join()
    p3.join()
    #生产者结束，——》q.join（）——》消费者确实把所有数据都收到
    #主进程结束之后，守护线程随之结束，这样消费者进程就不会存活

# 生产者消费者升级版