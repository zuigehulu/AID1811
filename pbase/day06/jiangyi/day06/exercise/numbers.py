#   1. 写一个程序,让用户输入两个以上的正整数,当输入负数时结束输入
#     (要求: 限制用户,不允许输入重复的数)
#     1) 打印这些数字的和
#     2) 打印这些数中最大的一个数
#     3) 打印这些数中第二大的一个数 
#     4) 删除最小的一个数

L = []  # 先创建一个列表容器用变量L绑定
while True:
    x = int(input("请输入正整数: "))
    if x < 0:  # 此处再次进行判断，查看已经获取的整数
        if len(L) > 2:
            break
        else:
            print("您输入的数字太少.请继续输入!!!")
            continue
    if x in L:  # if L.count(x) != 0: 判断x是否为输入过的数字?
        print("您已经输入过这个数了,请输入其它的数!")
    else:
        L.append(x)  # x第一次出现,加入到列表中

print(L)
print("这些数的和是:", sum(L))
print("最大的一个数是:", max(L))
# 求第二大的数 方法1 先删除最大的数,剩下的就是第二大的
zhuida = max(L)  # 先记下来最大的一个数
L.remove(max(L))
print("第二大的数是:", max(L))

L.append(zhuida)  # 再把最大数添加回来

L.remove(min(L))

print("最终的结果:", L)

