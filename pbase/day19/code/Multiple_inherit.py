class Plane:
    def fly(self,height):
        print("飞机以海拔",height,"米的高度飞行")
class Car:
    def run(self,speed):
        print("汽车以",speed,"公里／小时的速度行驶")

class Plane_Car(Plane,Car):
    pass

pc = Plane_Car()
pc.fly(200)
pc.run(20)
