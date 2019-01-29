# student_main
#主函数
from student_info import *
from student_menu import *
from student_shuchu import *
def main():
    L = Student.L
    read_txt(L)
    while True:
        qingping()
        jiemian()
        num = input("请进行操作:")
        if (num != '1' and num != '2' and 
            num != '3' and num != '4' and 
            num != '5' and
            num != 'q'):
            raise ValueError("没有此选项，请重新输入!")
        if num == '1':   #添加操作
            input_student(L)
        elif num == '2': #删除操作
            xinxi = input("请输入学生名字:")
            shanchu(xinxi,L)
        elif num == '3':        #查找操作
            xinxi = input("请输入学生名字:")
            chazhao(xinxi,L)
        elif num == 'q':
            return
        elif num == "4":  #显示学生全部信息
            xianshi_xueshengxinxi_jiemian(L)
            jieshoupaixu = input("请进行操作:")
            panduan_paixu(jieshoupaixu,L)
        elif num == '5' or num == 5:
            read_txt(L)
            input("文件导入已完成，请按回车继续")

def main_cuowu():
    while True:
        try:
            main()
        except ValueError as err:
            print(err)
        else:
            tuichu = input("确认退出？Ｎ／Ｙ")
            if tuichu == 'Y' or tuichu == 'y':
                break
        
       
main_cuowu()