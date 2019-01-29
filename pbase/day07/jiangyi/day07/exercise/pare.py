# 练习2:
#   已知有两个等长的列表:
#     list1 = [1001, 1003, 1008, 1004]
#     list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']
#   用list2中的元素作为键,用list1中对应的元素作为值,生成如下
#   字典
#     d = {'Tom': 1001, 'Jerry':1003, 'Spike': 1008,
#          'Tyke': 1004}


list1 = [1001, 1003, 1008, 1004]
list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']

# d = {k: v for k in list2 for v in list1}  此方法错误
# 方法1
# d = {}
# for i in range(len(list1)):
#     d[list2[i]] = list1[i]

# 方法2
# d = {}
# for k in list2:
#     d[k] = list1[list2.index(k)]

# 方法3
# d = {list2[i]: list1[i] for i in range(len(list1))}

# 方法4
d = {k: list1[list2.index(k)] for k in list2}
print(d)





# d = {'Tom': 1001, 'Jerry':1003, 'Spike': 1008,
#      'Tyke': 1004}
