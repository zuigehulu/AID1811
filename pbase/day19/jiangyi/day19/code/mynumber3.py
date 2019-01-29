# mynumber3.py

class MyNumber:
    '''自定义一个数字类,用来表示自己定义的数字信息'''
    def __init__(self, value):
        '''初始化方法'''
        self.data = value

    def __repr__(self):
        return 'MyNumber(%d)' % self.data

    def __int__(self):
        n = int(self.data)
        return n

n1 = MyNumber("100")
i = int(n1)  # i = 100
print('i=', i) # 100



