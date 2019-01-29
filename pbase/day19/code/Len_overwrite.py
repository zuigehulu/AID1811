class A:
    def __init__(self,l):
        self.l = [x for x in l]
    def __len__(self):
        s = len(self.l)
        return s
    def __repr__(self):
        return "A(%s)"%self.l
    def __abs__(self):
        L = [abs(x)for x in self.l]
        lst = A(L)
        return lst

    
a = A([1,2,3,-4,-5])
a1 =abs(a)
print(a)
print(len(a))
b = A('abcd')
print(b)
print(len(b))
print(a1)