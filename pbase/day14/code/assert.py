def get_score():
    s = int(input("请输入学生成绩"))
    assert 0<=s<=100,'成绩超出范围'
    return s
try:
    score = get_score()
except AssertionError as err:
    print("断言失败！，err=",err)