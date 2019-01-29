# 思考:
#   list类里提供了几个方法,但没有提供带有一个参数的头部添加数据
#   的方法,试题能否在不改变原列表类 list 的基础上,创建一个新的
#   类MyList类,新类继承原类全部的功能,并添加一个 
#     insert_head(n) 的方法

#   如:
#     class MyList(list):
#         def insert_head(self, n):
#             ...
#     myl = MyList(range(3, 6))
#     print(myl)  # [3, 4, 5]
#     myl.insert_head(2)
#     print(myl)  # [2, 3, 4, 5]
#     myl.append(6)
#     print(myl)  # [2, 3, 4, 5, 6]


class MyList(list):
    def insert_head(self, n):
        # self[0:0] = [n]
        self.insert(0, n)

myl = MyList(range(3, 6))
print(myl)  # [3, 4, 5]
myl.insert_head(2)
print(myl)  # [2, 3, 4, 5]
myl.append(6)
print(myl)  # [2, 3, 4, 5, 6]

