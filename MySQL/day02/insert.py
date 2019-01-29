# pymysql 的插入示例
from db_cint import *

try:
    try:
        conn = pymysql.connect(host,user,password,dbname)
        #获取游标
        cursor = conn.cursor()
        #执行sqlyu语句
        sql = ''' insert into acct values
        ('622345000011','Fisher','C0011',1,date(now()),1,33.0),
        ('622345000012','Bob','C0012',1,date(now()),1,30000.0),
        ('622345000013','Tom','C0013',1,date(now()),1,550.0);
        '''
        cursor.execute(sql)
        conn.commit
        print('OK')
    finally:
        cursor.close()
        conn.close()
except Exception as e:
    print('数据库插入异常')
    print(e)
