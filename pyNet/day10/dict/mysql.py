from pymysql import *

HOST = 'localhost'
USER = 'root'
PWD = '123456'
DNAME = 'dict'
db = connect(HOST,USER,PWD,DNAME)
if not db:
    print('连接数据库失败')
print('连接数据库成功')
cursor = db.cursor()
with open('dict.txt') as fr:
    while True:
        L = fr.readline()
        if not L:
            break
        word = L.split(' ')
        interpret =' '.join(word[1:]).strip()
        sql = 'insert into dict values(null,"%s","%s")'%(word[0],interpret)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
fr.close()
db.close()

    
