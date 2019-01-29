#账户管理系统,实现账户增删查改
import time

import pymysql

from db_cint import *

db_conn = None  #连接对象
#连接数据库
def conn_database():
    global db_conn
    db_conn = pymysql.connect(host,user,password,dbname)
    if not db_conn:
        print('连接数据库失败')
        return -1
    return 0

#查询账户，如果用户输入账号，则以用户账号查询，如果用户不输入账号则查询全部
def query_acct():
    acct_no = input('请输入要查询的账户')
    if acct_no and acct_no !='': #用户输入了账户
        sql = '''
            select * from acct where acct_no = '%s'
            '''%acct_no
    else:    #用户未输入账户名称，查询所有
        sql = '''
            select * from acct 
            '''
    #获取游标
    global db_conn
    cursor = db_conn.cursor()  #获取游标
    try:
        cursor.execute(sql)   #执行ＳＱＬ
        result = cursor.fetchall()
        for x in result:
            acct_no = x[0]
            acct_name = x[1]
            if x[6]:
                balance = float(x[6])
            else:
                balance = 0
            print("账户:%s,名称:%s,余额:%0.2f"
                  %(acct_no,acct_name,balance))
    except Exception as e:
        print('查询异常')
        print(e)
    return

#新增账户
def new_acct():
    try:
        while True:
            acct_no = input('请输入账号:')
            acct_name = input('请输入户名')
            acct_type = input('请选择账户类型(1.借记卡，２.理财卡)')
            balance = float(input('请输入开户金额'))
            if acct_no != '' and acct_name != '':
                break
            else:
                print("账号或户名不能为空!")
                time.sleep(2)
        assert acct_type in ['1','2']
        assert balance >= 10.00

        #拼装SQL语句，执行
        sql = '''
           insert into acct(acct_no,acct_name,acct_type,balance)
           values('%s','%s',%s,'%.2f')
        '''%(acct_no,acct_name,acct_type,balance)
        # 获取游标，执行
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql) #执行
        db_conn.commit #提交
        print('提交成功')
    except Exception as e:
        print('输入异常')
        print(e)
    return

#修改账户信息
def update_acct():
    try:
        cust_no = input('请输入户名')
        leixing = int(input('请输入您要修改的类别：１.户名　２.金额'))
        #　根据修改的内容形成sql语句
        if leixing == 1:
            acct_name = input('修改后的名字是:')
            sql = '''
                update acct set acct_name = '%s' where cust_no = '%s'
            '''%(acct_name,cust_no)
        elif leixing == 2:
            balance = float(input('修改的金额:'))
            sql = '''
                update acct set balance = %s where cust_no = '%s'
            '''%(balance,cust_no)
        else:
            print('输入错误，请重新操作')
            time.sleep(2)
            return
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)

        db_conn.commit()
        print("更新信息成功")
    except Exception as e:
        print("更新信息异常")
        print(e)

#删除账户
def del_acct():
    try:
        acct_no = input('请输出要删除的账户')
        sql = ''' 
            delete from acct where acct_no = '%s'
        '''%acct_no
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)
        db_conn.commit()
        print('删除成功')
    except Exception as e:
        print('删除失败')
        print(e)


# 账户界面
def print_menu():
    menu = '''
    ----------------账户管理系统-----------------
                １－查询账户信息
                ２－新建账户
                ３－修改账户
                ４－删除账户
                ５－退出
    '''
    print(menu)
    return     #结束标志

#关闭数据库
def close_database():
    global db_conn
    if db_conn:
        db_conn.close()
 
#验证账号密码
def yanzheng_mima():
    dbname1 = 'users'
    try:
        conn = pymysql.connect(host,user,password,dbname1)
        name = input('请输入账号:')
        pass_word = input('请输入密码:')
        sql ='''
             select user_name, user_id 
             from user_table where user_name = '%s' and user_pd = '%s';
        '''%(name,pass_word)
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        if result :
            return 0
        else:
            return -1
    except Exception as e:
        print('查询账号密码失败')
        print(e)
        return -2

    
#main
def main():
    #验证账号密码信息
    if yanzheng_mima() < 0:
        print('认证失败，账户或密码错误')
        return
    #第一步，连接数据库
    if conn_database() < 0:
        return
    #第二步，循环打印菜单　根据选择的菜单调用不同的函数进行处理
    while True:
        print_menu()
        oper = input("请选择操作:")
        if not oper:
            continue
        if oper == '1': #查询
            query_acct()
        elif oper =='2': #新建
            new_acct()
        elif oper =='3': #修改
            update_acct()    
        elif oper =='4': #删除
            del_acct()  
        elif oper =='5': #退出
            break
        else:
            print("请输入正确的值")
            time.sleep(2)
            continue  
    #第三步，关闭数据库
    close_database()
#主函数
if __name__ == '__main__':
    main()

