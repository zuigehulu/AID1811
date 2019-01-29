class MyNumber:
    def __init__(self,data):
        self.data = data
    def __repr__(self):
        return 'M(%s)'%self.data
    def __sub__(self,rhs):
        if type(self.data) is int:
            s = self.data - rhs.data
            return MyNumber(s)
        else:
            raise ValueError("错了错了错了")
    
n1 = MyNumber(100)
n2 = MyNumber(200)
n3 = n1 - n2
n4 = n2 - n1
print(n3)
print(n4)
L1 = MyNumber([200])
L2 = MyNumber([100])
L3 = L2 - L1
print(L3)