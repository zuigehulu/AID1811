class MyRange:
    def __init__(self,start,stop=None,step=1):
        # if step <= 0 and start < stop:
        #     assert ValueError
        # elif step >=1 and start > stop:
        #     assert ValueError
        # elif step == 0:
        #     assert ValueError
        if stop == None:
            self.stop = start
            self.start = 0
            self.step = step
        else:
            self.start = start
            self.stop = stop
            self.step = step
        # self.L = [x for x in range(self.start,self.stop,self.step)]
    def __iter__(self):
        return MyRange(self.start,self.stop,self.step)
        # return MyRamgeInfo(self.start,self.stop,self.step)
    def __next__(self):
        if self.step > 0:
            if self.start >= self.stop:
                raise StopIteration
            r = self.start
            self.start += self.step
            return r
        elif self.step < 0:
            if self.start <= self.stop :
                raise StopIteration
            r = self.start
            self.start += self.step
            return r
        else:
            raise ValueError
# class MyRamgeInfo:
#     def __init__(self,start,stop,step):
#         self.start = start
#         self.stop = stop
#         self.step =step
#         self.index = 0
#     def __next__(self):
#         # if self.index >= len(self.L):
#         #     raise StopIteration
#         # r = self.L[self.index]
#         # self.index += 1
#         # return r

        
a = MyRange(5)
# b = a.__iter__()
print(next(a))
# next(a)
# print(a.__next__())
# # print(next(a))

L= list(MyRange(5))
print(L) #[0,1,2,3,4,5]
print(sum(MyRange(1,101)))
L2 = [x**2 for x in MyRange(1,10,3)]
print(L2)
for x in MyRange(10,0,-3):
    print(x)