class Car:
    def __init__(self,info):
        self.info = info
        print("汽车%s对象被创建"%info)
    def __del__(self):
        print("汽车：%s对象被销毁"%self.info)
    
c1 = Car("BYD E6")
input("请输入回车键继续")
print("程序正常运行")