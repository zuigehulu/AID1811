# # pymysql 查询示例是
#   　第一步：导入pymysql模块

from db_cint import *
#     第二步：建立到数据库服务器的连接，创建连接对象
# host = 'localhost' 
# user = 'root'
# password = '123456'
# dbname = 'bank'
conn = pymysql.connect(host,user,password,dbname)

#     第三步：创建游标对象（cursor）,通过调用数据库连接对象获得游标
cursor = conn.cursor() #获得游标
#     第四步：利用cursor对象，执行SQL语句
sql = 'select * from acct'
cursor.execute(sql)  #执行sql语句
#取出一行打印
resu = cursor.fetchone()
print(resu)
#取出查询结果并打印
result = cursor.fetchall()

for x in result:
    acct_no = x[0]
    acct_name = x[1]
    if x[6]:
        balance = float(x[6])
    else:
        balance = 0
    print('账号:%s,户名:%s,余额:%.2f'%(acct_no,acct_name,balance))
#     第五步：提交事务（如果需要）
#     第六步：关闭游标对象
cursor.close()
#     第七步：关闭数据库连接对象
conn.close()
