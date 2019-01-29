class Human:
    '''定义一个人类的基类'''
    def say(self,what):
        print('说',what)
    def walk(self,distance):
        print("走了:",distance,'公里')
class Student(Human):
    def study(self,subject):
        print('学习',subject)
    
class Teacher(Human):
    def teach(self,subject):
        print("教",subject)
h1 = Human()
h1.say("天气变冷了")
h1.walk(5)
h2 = Student()
h2.say("真傻")
h2.study('玩游戏')
print("-------------------------")
h3 = Teacher()
h3.walk(10)
h3.teach("电脑")


