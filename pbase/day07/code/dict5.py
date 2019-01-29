jingli = {"曹操","刘备","孙权"}
jishu = {"曹操","孙权","张飞","关羽"}

s = jishu & jingli 
d = jishu - jingli
e = jingli - jishu
zhangfei = '张飞' in jingli
liangbu = jishu ^ jingli
zong = jishu | jingli
print(s)
print(d)
print(e)
print(zhangfei)
print(liangbu)
print(zong)