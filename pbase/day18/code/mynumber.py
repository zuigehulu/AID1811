class MyNumber:
    def __init__(self,value):
        self.data = value
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return 'MyNumber(%d)'%self.data

n1 = MyNumber(100)
print(str(n1))
print(repr(n1))
n2 = MyNumber(200)