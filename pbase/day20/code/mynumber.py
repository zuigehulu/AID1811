class MyNumber:
    def __init__(self,value):
        self.data = value
    def __repr__(self):
        return "MN(%s)"%self.data
    def __add__(self,n):
        s = self.data + n.data
        return MyNumber(s)
    
n1 = MyNumber([100])
n2 = MyNumber([200])
print(n1)
print(n2)
# n3 = n1.add(n2)
n3 = n1+n2 #等同于　n3 = n1__add__(n2)
print(n3)