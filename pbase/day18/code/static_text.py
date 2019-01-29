def A(v = 0):
    return v
# A.get_v()
def zhuangshiqi():
    return get_v(A)

@zhuangshiqi
def get_v(cls):
    s = A() # s = class()
    return s
print(get_v())