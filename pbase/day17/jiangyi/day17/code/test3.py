# class des(list):
#     def __call__(self,num):
#         return self[num]
    
# L = [1,2,3,4]
# d = des()
# d = [1,2,3,4,5]
# print(d[2])

class Mylist:
    def __init__(self,l):
        self.lst = [x for x in l]
    def __repr__(self):
        return '%s'%self.lst
    def __getitem__(self,i):
        return self.lst[i]
