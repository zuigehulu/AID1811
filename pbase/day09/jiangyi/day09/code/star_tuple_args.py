# star_tuple_args.py


# 此示例示意星号元组形参的定义及使用
def func(*args):
    print("实参个数是:", len(args))
    print("args=", args)

func()
func(1, 2, 3, 4)
func(1, 2, 3, 4, 'AAA', 'BBB')
func(*"ABCDEFG")  # func('A', 'B', ....'G')
