# default_args.py

# 此示例示意函数的缺省参数
def info(name, age=1, address='不详'):
    print(name, '今年', age, '岁, 家庭住址:', address)

info("魏明择", 35, '北京市朝阳区')
info("Tarena", 15)
info("小张")
# info()  # 出错
