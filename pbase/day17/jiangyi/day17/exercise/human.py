# 练习:
#   1. 定义一个 '人' 类
#     class Human:
#         def set_info(self, name, age, address='不详'):
#             '此方法为self对象添加姓名,年龄,家庭住址属性'
#             ... # 此处自己实现
        
#         def show_info(self):
#             '此方法显示某个人(实例)的信息'
#             ... # 此处自己实现
#     h1 = Human()
#     h1.set_info('小张', 20, '北京市朝阳区')
#     h2 = Human()
#     h2.set_info('小李', 18)
#     h1.show_info()  # 小张 今年 20 岁,家庭住址: 北京市朝阳区
#     h1.show_info()  # 小李 今年 18 岁,家庭住址: 不详


class Human:
    def set_info(self, name, age, address='不详'):
        '此方法为self对象添加姓名,年龄,家庭住址属性'
        self.name = name
        self.age = age
        self.address = address
    
    def show_info(self):
        '此方法显示某个人(实例)的信息'
        print(self.name, '今年', self.age,
              '岁,家庭住址:', self.address)

h1 = Human()
h1.set_info('小张', 20, '北京市朝阳区')
h2 = Human()
h2.set_info('小李', 18)
h1.show_info()  # 小张 今年 20 岁,家庭住址: 北京市朝阳区
h2.show_info()  # 小李 今年 18 岁,家庭住址: 不详

# 思考?
# h3 = Human('小王', 19, '上海市浦东新区')

# lst3 = list("ABCD")

