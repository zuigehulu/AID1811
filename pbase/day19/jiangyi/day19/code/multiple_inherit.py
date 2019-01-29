# multiple_inherit.py

import pdb

class Plane:
    def fly(self, height):
        print("飞机以海拔", height, '米的高度飞行')

class Car:
    def run(self, speed):
        print("汽车以", speed, '公里/小时的速度行驶')

class PlaneCar(Plane, Car):
    'PlaneCar 继承自Plane 和 Car类'

p1 = PlaneCar()
p1.fly(10000)
p1.run(300)








