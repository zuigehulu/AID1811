class Human:
    def set_info(self,name,age,address='不详'):
        self.name = name
        self.age = age
        self.address = address
    def show_info(self):
        print('%s今年%s岁,家庭住址:%s'%(self.name,
               self.age,self.address))

h1 = Human()
h1.set_info("小张",20,'北京市朝阳区')
h2 = Human()
h2.set_info("小李",18)
h1.show_info()
h2.show_info()
h3 = Human("小王",19)