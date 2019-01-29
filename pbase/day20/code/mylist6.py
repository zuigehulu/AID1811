#示意重载索引／切片运算符[]的重载
class MyList:
    def __init__(self,iter):
        self.lst = [x for x in iter]
    def __repr__(self):
        return  "MyList(%s)"%self.lst
    def __getitem__(self,i):
        return self.lst[i]
    def __setitem__(self,i,v):
        self.lst[i] = v
        return self
    def __delitem__(self,i):
        del self.lst[i]
        return self

L1 = MyList([1,-2,3,-4,5])
v = L1[2]
L1[1] = 2
print(v)
print(L1)
del L1[3]
print(L1)