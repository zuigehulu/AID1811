# inherit.py

# 此示例示意继承的语法和用法

class Human(object):
    '''定义人类的基类'''
    def say(self, what):
        print("say:", what)

    def walk(self, distance):
        print("走了:", distance, '公里')

class Student(Human):
    def study(self, subject):
        print("学习:", subject)

class Teacher(Human):
    def teach(self, subject):
        print("教:", subject)


h1 = Human()
h1.say('天气变冷了')
h1.walk(5)
print("-------- 以下是学生的行为------")
s1 = Student()
s1.walk(4)
s1.say("感觉有点累")
s1.study("面向对象")
print('--------以下是教师的行为--------')
t1 = Teacher()
t1.teach("继承/派生")
t1.walk(6)
t1.say("今天吃点什么!!")






