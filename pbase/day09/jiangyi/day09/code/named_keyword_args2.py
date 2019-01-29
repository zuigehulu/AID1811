# named_keyword_args.py

# 此示例示意命名关键字形参的定义方法和调用传参
def func1(a, b, *args, c, d):
    print(a, b, args, c, d)


# func1(1, 2, 3, 4)  # <<< --- 此处出错
func1(11, 22, d=44, c=33)
func1(a=1, b=2, c=3, d=4)
func1(1, 2, 3, 4, c=300,d=400)
