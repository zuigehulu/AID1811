# # 1 1 2 3 5 8 13 ....要求将这些数的存在宇一个列表中，前４０个
# L =[1,1]
# x = 1
# y = 1
# i = 3
# while True:
#     sum = x + y
#     y = x
#     x = sum 
#     i += 1
#     if i >= 40:
#         break
#     L += [sum]
# print(i)
# print(L)
l = [1,1]
while len(l) < 40:
   l.append(l[-1]+l[-2])
print(l)
