# mynumber.py

class MyNumber:
    '''自定义一个数字类,用来表示自己定义的数字信息'''
    def __init__(self, value):
        '''初始化方法'''
        self.data = value

    def __str__(self):
        return "数字: " + str(self.data)
    
    def __repr__(self):
        return 'MyNumber(%d)' % self.data

n1 = MyNumber(100)
print(str(n1))  # 数字: 100, str(n1)相关于 n1.__str__()


