# dict_keyword_args.py

# 此示例示意字典关键字形参
def func(**kwargs):
    print("关键字参数的个数是:", len(kwargs))
    print("kwargs= ", kwargs)

func(name='魏明择', age=35, address='朝阳区')
func(a=1, b=2, c=3, d="ABC", e=[1, 2, 3])



