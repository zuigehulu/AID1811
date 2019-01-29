s = {"唐僧","悟空","八戒","沙僧"}
#用while　语句的迭代器实现
it = iter(s)
while True:
    try:
        s = next(it)
        print(s)
    except StopIteration:
        print("遍历结束")
        break
    