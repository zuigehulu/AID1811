def input_number():
    d = []
    while True:
        a = int(input("输入一个正整数"))
        if a < 0:
            break
        # d +=[a]
        d.append(a)
    return d
c = input_number()
print("用户输入的最大值是:",max(c))
print("用户输入的最小值是:",min(c))
print("用户输入的和是:",sum(c))

