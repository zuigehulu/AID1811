# 练习:
#   自己写一个文件 info.txt 内部写入如下一些文字信息
#     张三 20 100
#     李四 21 96
#     小王 22 98
#   写程序将这些数据读取出来,并以如下格式打印在屏幕终端上
#     张三 今年 20 岁,成绩是: 100
#     李四 今年 21 岁,成绩是: 96
#     小王 今年 22 岁,成绩是: 98

def read_info(filename):
    '''读取filenamem 内容,形成字典的列表返回 
    返回: [
          {'name': '张三', 'age': 20, 'score': 100},
          {'name': '李四', 'age': 21, 'score': 96},
          {'name': '小王', 'age': 22, 'score': 98},
          ]
    '''
    L = []
    try:
        fr = open(filename)
        while True:
            s = fr.readline() # '张三 20 100\n'
            if not s:
                break
            s2 = s.rstrip()  # '张三 20 100' 去掉右边的空白字符?
            n, a, s = s2.split()  # ['张三', '20', '100']
            a = int(a)
            s = int(s)  # 转为整数
            L.append(dict(name=n, age=a, score=s))

        fr.close()
    except OSError:
        print("读取数据失败")
    return L

infos = read_info('info.txt')
# print(infos)

def print_info(infos):
    for d in infos:
        print(d['name'], '今年',
              d['age'], '岁,成绩是:',
              d['score'])

print_info(infos)
