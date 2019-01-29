def get_score():
    score= int(input("请输入学生成绩(0-100)："))
    if 0 < score < 100:
        return score
    return 0
def get_get_score():
    try:
        score = get_score()
    except ValueError:
        print("输入错误，成绩变成０！")
        return 0
    else:
        return score
score = get_get_score()
print("学生成绩是:",score)