import re

#re.I　忽略大小写
# s = 'Hello World'
# pattern = r'hello'
# regex = re.compile(pattern,flags=re.I)

#re.A使用ASCII字符
# s = 'Hello 你好'
# pattern = '\w+'
# regex = re.compile(pattern,flags=re.A)

#re.S使用.匹配\n
# s = '''Hello world
# nihao China
# '''
# pattern = r'.+'
# regex = re.compile(pattern,flags=re.S)

#M匹配每行开头结尾
# s = '''Hello world
# nihao China
# '''
# pattern = r'^nihao|world$'
# regex = re.compile(pattern,flags=re.M)

#X给正则加注释
s = 'abcdef'
pattern = r'''(ab)  #第一行分组
\w+  #任意字符串
(?P<dog>ef)   #dog组
'''
regex = re.compile(pattern,flags=re.X)

l = regex.findall(s)
print(l)