#自定义一个环境管理器，让其能被with语句管理
class A:
    
    def __enter__(self):
        print("A.enter方法被调用")
        self.file = open('test.txt')
        return self
    def __exit__(self,e_type,e_value,e_cb):
        self.file.close()
        print("A.__exit__被调用，已离开with语句")
        if e_type is None:
            print("正常离开")
        else:
            print("异常类型",e_type)
            print("异常对象",e_value)
            print("追踪对象",e_cb)
with A() as a:
    print(a.file.readline())
    3/0
    print("这是with语句内部的语句")