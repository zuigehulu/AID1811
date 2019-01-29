# 此示例示意sys.stdin的用法


import sys
# s = input("请输入: ")  # input函数内部调用sys.stdin.readline()

s = sys.stdin.readline()
print("您刚才输入的是:", s)

sys.stdin.close()

s2 = input("请输入: ")  # 关闭stdin后, input将不再可用
print("s2=", s2)