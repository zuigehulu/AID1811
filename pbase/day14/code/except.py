#此示例用try-except语句来捕获异常，处理错误，将程序
import time
def div_apple(n):
    print("%d个苹果，您想分给几个人?"%n)
    s = input("请输入人数:")
    count = int(s)
    result = n/count
    print("每个人分了%s个苹果"%result)
def try_ceshi(n):
    try:
        if n == 0:
            print("你个笨蛋，苹果都吃不到")
            
        else:
            div_apple(n)
            print("分苹果成功")
    except ValueError as shibai:
        print("分苹果失败，苹果让老巫婆吃掉了１个s")
        # time.sleep(5)
        try_ceshi(n-1)
    except ZeroDivisionError:
        print("没有人来，苹果烂掉了")
    except:
        print("错误已捕获，很古怪的错误")
    else:
        print("你猜我会打印几次？",n)
    finally:
        print("你再猜猜我会打印几次",n)
try_ceshi(5)
print("程序正常结束")