class Shape:
    def draw(self):
        print("Shap.draw()方法被调用")

class Point(Shape):
    def draw(self):
        print("正在画一个点！！！")

class Circle(Point):
    def draw(self):
        print("正在画一个园")

def my_draw(s):
    s.draw()  #此处调用谁

s1 = Circle()
s2 = Point()
s3 = Shape()
s4 = 0 
my_draw(s1)
my_draw(s2)
my_draw(s3)
my_draw(s4)