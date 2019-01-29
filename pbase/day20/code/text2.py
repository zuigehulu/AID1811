# 实现有序集合类 OrderSet() 能实现两个集合的交集　&
# 并集| 补集 - 对称补集 ^, ==,!= in ,not in 等操作
# 要就：集合内部用list存储数据
class OrderSet:
    def __init__(self,val):
        self.val = [x for x in val]
    def __repr__(self):
        return 'OrderSet(%s)'%self.val
    def __and__(self,rhs):
        L = []
        for x in self.val:
            if x in rhs.val:
                L.append(x)
        return OrderSet(L)
    def __or__(self,rhs):
        L = []
        for x in self.val:
            if x not in rhs.val:
                L.append(x)
        L.extend(rhs.val)
        return OrderSet(L)
    def __xor__(self,rhs):
        L = []
        for x in self.val:
            if x not in rhs.val:
                L.append(x)
        for x in rhs.val:
            if x not in self.val:
                L.append(x)
        return OrderSet(L)
    def __ne__(self,rhs):
        if self.val != rhs.val:
            return True
        else:
            return False
    def __eq__(self,rhs):
        if self.val == rhs.val:
            return True
        else:
            return False
    def __contains__(self,rhs):
        if rhs in self.val:
            return True
        else:
            return False
            
s1 = OrderSet([1,2,3,4])
s2 = OrderSet([3,4,5])
print(s1 & s2) #OrderSet([3,4])
print(s1 | s2) #OrderSet([1,2,3,4,5])
print(s1 ^ s2) #OrderSet([1,2,5])
if OrderSet([1,2,3]) != s1:
    print("不等于")
else:
    print("等于")
if s2 == OrderSet([3,4,5]):
    print('s2 == OrderSet([3,4,5])')
if 2 in s1:
    print('2 in s1')
    