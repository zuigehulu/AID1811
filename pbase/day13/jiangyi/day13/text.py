s = '1+2'
s1 = 'a+b'
print(eval(s1,{'a':100,'b':200}))
print(eval(s))
print(eval(s1,{'a':200},{'b':20}))
