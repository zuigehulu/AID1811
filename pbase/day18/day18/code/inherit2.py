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

class Teacher(Student):
    def teach(self, subject):
        print("教:", subject)


s1 = Student()
s1.say("感觉有点累")

t1 = Teacher()
t1.say('昨天圣诞节')
t1.study('转魔方')









