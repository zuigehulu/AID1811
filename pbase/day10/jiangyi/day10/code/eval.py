# eval.py

s1 = "1 + 2 * 3"  # s1是符合python语法规则的字符串
s2 = 'x + y'

v = eval(s1)
print(v)  # 7

x = 100
y = 200
v2 = eval(s2)
print('v2=', v2)

v2 = eval(s2, {'x':10, 'y':20})
print(v2)  # 30

v2 = eval(s2, {'x': 10, 'y': 20}, {'y': 2})
print('v2=', v2)  # 12


