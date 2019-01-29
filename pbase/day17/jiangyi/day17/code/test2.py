class car:
    def __init__(self,n,c,su):
        self.name = n
        self.color = c
        self.sudu = su
    def info(self):
        print(self.color,'的',self.name,'行驶速度是',self.sudu)
    
c1 = car('奥迪','红色',150)
c1.info()
print(c1.__dict__)
print(c1.__class__)
L = []
print(L.__class__)
c3 = c1.__class__('奥拓','黄色','30')
c3.info()

c2 = car('奥迪','白色',180)
c2.info()