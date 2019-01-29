class A(): 
    def __init__(self): 
        self.__a=None 
    @property 
    def a(self): 
        return self.__a 
class B(A): 
    def __init__(self): 
        super().__init__ 
    def printa(self): 
        super().a=11 
        print(super().a) 
        
b=B() 
b.printa()
