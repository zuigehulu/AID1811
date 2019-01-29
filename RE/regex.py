import re

pattern = r"(\w+):(\d+)"
s = "张:1994,李:1995"

#直接用re调用
# l = re.findall(pattern,s)
# print(l)

#通过compile对象调用
# regex = re.compile(pattern)
# l = regex.findall(s,pos=0,endpos=10)
# print(l)

#按正则表达式内容进行切割
# l = re.split(r'\,+',"Hello,   world nihao, Kitty")
# print(l)

#sub 进行替换
s = re.subn(r'\s+','##','hello word  nihao   Kitty',2)
print(s)

