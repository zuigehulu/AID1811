import pymysql

from db_cint import *

try:
    conn = pymysql.connect(host,user,password,dbname)
    cursor = conn.cursor()
    sql = ''' update acct set
    balance = balance + 1000
    where acct_no = '622345000013' 
    '''
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount)
except Exception as e:
    print('错误')
    print(e)
finally:
    cursor.close()
    conn.close()