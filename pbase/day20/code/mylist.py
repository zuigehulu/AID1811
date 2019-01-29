class MyList:
    def __init__(self,iter):
        self.lst = [x for x in iter]
        print('idid:',id(self.lst))
    def __repr__(self):
        return  "MyList(%s)"%self.lst
    def __add__(self,rhs):
        s = self.lst + rhs.lst
    def __iadd__(self,rhs):
        print('id',id(self.lst))
        self.lst.extend(rhs.lst)
        print(id(self.lst),'id')
        return self
L1 = MyList([1,2,3])
L2 = MyList(range(4,7))
print('L1id:',id(L1))
L1 += L2
print(L1)
print(id(L1))