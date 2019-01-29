# student_menu
#添加界面
def jiemian():
        print("1.添加学生信息")
        print("2.删除学生信息")
        print("3.查找学生信息")
        print("4.显示全部信息")
        print("5.从文件中读取数据（s1.txt）")
        print("7.退出(q)")

#显示里的菜单
def xianshi_xueshengxinxi_jiemian(L):
    qingping()
    print("1.按成绩从大到小显示")
    print("2.按成绩从小到大显示")
    print("3.按年龄从大到小显示")
    print("4.按年龄从小到大显示")
    print("5.(q)返回主列表")

#清屏
def qingping():
    import os
    os.system('clear')
