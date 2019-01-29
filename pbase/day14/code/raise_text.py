def get_age():
    try:
        age = int(input("请输入您的年龄(1-140):"))
    except ValueError:
        err = ValueError("您输入的是啥?")
        raise err
    if 1 <= age <= 140:
        return age
    else:
        err = ValueError("您输入的是啥?")
        raise err
try:
    age = get_age()
    print("您输入的年龄是:%s"%age)
except ValueError as err:
    print(err)

