s1 = "1 + 2 * 3" #s1必须是符合python3语法规则的字符串
s2 = "x + y"
v = eval(s1)
x = 100 
y = 200
v1 = eval(s2)
print(v)
print(v1)
v1 = eval(s2,{'x':10,'y':20})
print(v1)
v1 = eval(s2,{'x':10,'y':20},{'y':2})
print(v1)