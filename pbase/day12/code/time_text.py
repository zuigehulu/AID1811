import time
chusheng = input('请输入你的生日(年,月,日)')
chusheng1 = chusheng.split(',')
yuanzu = (int(chusheng1[0]),int(chusheng1[1]),int(chusheng1[2]),0,0,0,0,0,0)
miaoshu = time.time() - time.mktime(yuanzu)
tian = int(miaoshu/60/60//24)
print("您已经出生%d天"%tian)
week = {
    0:'一',
    1:'二',
    2:'三',
    3:'四',
    4:'五',
    5:'六',
    6:'日'
}
xingqi = time.localtime(time.mktime(yuanzu))
print('您出生日期是星期%s'%week[xingqi[6]])
