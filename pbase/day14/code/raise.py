import time
def make_except():
    print("开始....")
    time.sleep(1)
    error = ValueError("开始燥")
    raise error  #触发一个错误对象
    print(time.asctime())
    print("结束....")
try:
    make_except()
except ValueError as error:
    print("%d自作孽不可活",error)
print("程序正常结束")