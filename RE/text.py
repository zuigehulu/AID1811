import re

string = ''
with open('txt.txt') as fr:
    for x in fr:
        string += x

# pattern = '\b[A-Z]+\w*'
# l = re.findall(pattern,string)
# print(l)

#小数／分数／数字／负数百分数 
# pattern1 = r'-*\d+\.[0-9,/,%,\.]+\d*|[1-9,-]+[0-9,/,%,//]+\.*\d*|[0-9]'
pattern1 = r'-?\d+\.?\d*%?'
l1 = re.finditer(pattern1,string)
for x in l1:
    print(x.group())