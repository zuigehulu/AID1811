l = []
j = 1
while True:
    num = int(input("输入第%d个正整数(最少输三个，－１结束):"%j))
    if num < 0:
        if len(l) > 2:
            break
        else:
            print("您输入的太少，请重新输入")
            continue
    # if num not in l:
    #     l += [num]
    # else:
    #     print("您输入的数字已重复，请重新输入")
    #     continue
    if l.count(num) <= 0:
        l +=[num]
    else:
        print("您输入的数字已重复，请重新输入")
        continue
    j += 1
print(l,id(l))
print(sum(l))
print(max(l))
max1 = max(l)
l.remove(max1)
print(max(l))
min1 = min(l)
l.remove(min1)
print(l)
print(id(l))