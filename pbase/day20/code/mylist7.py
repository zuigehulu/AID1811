#示意重载索引／切片运算符[]的重载
class MyList:
    def __init__(self,iter):
        self.lst = [x for x in iter]
    def __repr__(self):
        return  "MyList(%s)"%self.lst
    def __getitem__(self,i):
        print('i=:',i)
        return self.lst[i]

L = MyList([1, 2, 3, 4, 5])
print(L[0::2])