class Mylist(list):
    def insert_head(self,n):
        self.reverse()
        self.append(n)
        self.reverse()

myl = Mylist(range(3,6))
print(myl)
myl.insert_head(2)
print(myl)