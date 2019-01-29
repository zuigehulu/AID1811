# 此示例示意函数的缺省参数lst=[] 列表会在def语句执行时
# 创建,并一直绑定,不会被释放,因此可能会引起函数不可重入问题
# 改进方法见:
#      function_default_args2.py
# 改进前
# L = [1, 2, 3]
# def f(n=0, lst=[]):
#     lst.append(n)
#     print(lst)

# 改进后
L = [1, 2, 3]
def f(n=0, lst=None):
    if lst is None:
        lst = []  # 创建一个新列表并绑定
    lst.append(n)
    print(lst)


f(4, L)  # [1, 2, 3, 4]
f(5, L)  # [1, 2, 3, 4, 5]
f(100)   # [100]
f(200)   # [200]
