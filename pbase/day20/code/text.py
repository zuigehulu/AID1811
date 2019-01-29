class MyList:
    def __init__(self,iter):
        self.lst = [x for x in iter]
    def __repr__(self):
        return  "MyList(%s)"%self.lst
    def __add__(self,rhs):
        s = self.lst + rhs.lst
        return MyList(s)
    def __mul__(self,rhs):
        s = self.lst * rhs
        return MyList(s)
    def __rmul__(self,lhs):
        print('rmul被调用')
        s = self.lst * lhs
        return MyList(s)
    
L1 = MyList([1,2,3])
L2 = MyList(range(4,7))
L3 = L1 + L2
print(L3)  #MyList([1,2,3,4,5])
L4 = L2 + L1
print(L4)
L5 = L1 * 2
print(L5)
L6 = 2 * L1
print(L6)
