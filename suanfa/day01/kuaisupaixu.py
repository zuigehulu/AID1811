value = [80,70,30,50,69,78,90,100,65,88]

def kuaisu(value):
    if len(value) < 2:
        return value
    #设置关键数据
    mark = value[0]
    # 找出所有小于关键数据的
    small = [x for x in value if x < mark]
    #　找出所有大于关键数据的
    equal = [x for x in value if x == mark]
    #　找出所有等于关键数据的
    big = [x for x in value if x > mark]

    #从小到大排序
    return kuaisu(small) + equal +kuaisu(big)

print(kuaisu(value))
