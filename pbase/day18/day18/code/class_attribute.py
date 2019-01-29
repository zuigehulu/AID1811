# class_attribute.py


class Human:
    '''此示例示意类属性'''
    count = 0  # 创建类属性(类变量)

print(Human.count)  # 获取类属性绑定的值
Human.count = 100  # 修改类属性
print(Human.count)  # 100



