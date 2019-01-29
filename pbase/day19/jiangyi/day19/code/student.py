# student.py

class Student:
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s
    
    # def __repr__(self):
    #     print("__repr__ 方法被调用!")
    #     return "asd"
    def __str__(self):
        return "Student('%s', %d, %d)" % (self.name,
                self.age, self.score)
        
L = []
L.append(Student('小张', 20, 100))
L.append(Student('小李', 18, 98))
print(L)  # [Student('小张', 20, 100), Student('小李', 18, 98)]

