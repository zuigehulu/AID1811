# 写代码，有如下变量，请按照要求实现每个功能
# 　　　name = "　　gougouQ　　"
# 1.移除name变量对应值的两边的空格，并输出移除后的内容
# 2.判断name变量对应的值是否以"go"开头
# 判断name变量对应的值是否以"Q"结尾
# 将name变量对应的值重'o',替换为'p',并
name = "    gougouQ   "
name1=name.split()
name2 = name.startswith("go")
name3 = name.endswith("Q")
name4 = name.replace("o","P")





name = "  gougouQ  "
name1 = name.split()
name2 = name.startswith("go")
name3 = name.endswith('Q')
name4 = name.replace("o","p")
print(name1)
print(name2)
print(name3)
print(name4)