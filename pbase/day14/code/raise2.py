import time
def make_except():
    print("开始....")
    time.sleep(1)
    raise ValueError
    print(time.asctime())
    print("结束....")
try:
    make_except()
except ValueError :
    print("%d自作孽不可活")
print("程序正常结束")