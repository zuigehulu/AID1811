from pymongo import MongoClient

#创建数据库链接
conn = MongoClient('localhost',27017)

#创建数据库对象
db = conn.stu

#创建集合对象
myset = db['class4']

#操作数据
# print(dir(myset))

#插入文档
# myset.insert_one({'name':'张铁林','King':'乾隆'})
# myset.insert_many([{'name':'张国立','King':'康熙'},{'name':'程道明','King':'康熙'}])
# myset.insert({'name':'唐国强','King':'雍正'})
# myset.insert([{'name':'程建斌','King':'雍正'},{'name':'聂远','King':'乾隆'}])
# myset.save({'_id':'1','name':'郑少秋','King':'乾隆'})

#获取游标对象
cursor = myset.find({},{'_id':0})
# print(cursor)
#循环获取每一条文档
# for x in cursor:
#     print(x['name'],'--------',x['King'])

# print(cursor.next()) #获取下一个文档

#跳过第一个取后面３个文档
# for i in cursor.skip(1).limit(3):
#     print(i)

#注意　排序写法同mongo shell不同，用元组表达
# for i in cursor.sort([('name',1)]):
    # print(i)

# dic ={'$or':[{'King':'乾隆'},{'name':'程道明'}]}
# d=myset.find(dic,{'_id':0})
# for i in d:
#     print(i)

# myset.update_one({'King':'康熙'},{'$set':{'king_name':'玄烨'}},upsert=True)

# myset.update_many({'King':'乾隆'},{'$set':{'king_name':'弘历'}},upsert=True)


#删除操作
# myset.delete_one({'King':'乾隆'})
# myset.delete_many({'king_name':{'$exists':False}})

#复合操作
print(myset.find_one_and_delete({'name':'郑少秋'}))

#关闭链接
conn.close()