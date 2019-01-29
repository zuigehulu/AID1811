class A(): 
    __a=None 
    
    @property 
    def a(self): 
        return self.__a 
       
class B(A):
    def printa(self): 
        A.a=11
        print(super().a) 
b=B() 
b.printa()
