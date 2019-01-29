
while True:
    num = input("请输入密码:")
    num = num.strip()
    if num.isdigit():
        print("过于简单")
        continue
    elif num.isalpha():
        print("不能全是字母")
        continue
    else:
        print("欢迎您的到来")
        break
