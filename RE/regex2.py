import re

pattern = r'(?P<piglet>ab)cd(?P<dog>ef)'

regex = re.compile(pattern)

#获取match对象
obj = regex.search('abcdefghijk',pos=0,endpos=8)
#obj属性变量
print(obj.pos) #目标字符串的开始位置
print(obj.endpos)#目标字符串的结束位置
print(obj.re)  #目标正则表达式
print(obj.string) #最原始的字符串（未截取的）
print(obj.lastgroup) #最后一组的名称
print(obj.lastindex) #最后一组是第几组
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
#obj方法
print(obj.span())  #得到匹配内容的起止位置
print(obj.start())  #得到匹配内容的开始位置
print(obj.end())   #得到匹配内容的结束位置

print(obj.group()) #整体匹配内容
print(obj.group(1)) #第一组的内容
print(obj.group(2))  #第二组内容
print(obj.group('dog')) #dog组内容

print(obj.groupdict()) #获取捕获组
print(obj.groups()) #获取所有子组
