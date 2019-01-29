class MyNumber:
    def __init__(self,val):
        self.val = val
    def __int__(self):
        i = int(self.val)
        return i

n1 = MyNumber("100")
i = int(n1)
print('i',i)