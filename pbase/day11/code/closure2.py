# def pow2(x):
#     return x**2
# def pow3(x):
#     return x**3
# def pow4(x):
#     return x**4
# def pow5(x):
#     return x**5   需求
def make_power(y):
    def fn(x):
        return x ** y
    return fn
pow2 = make_power(2)
print(pow2(3))
print(pow2(5))