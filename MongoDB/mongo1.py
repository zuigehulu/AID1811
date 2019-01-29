from pymongo import MongoClient
import random

conn = MongoClient('localhost',27017)

db=conn.stu

myset = db.class0

#数据操作
# index_name = myset.create_index('name')
# index_name = myset.create_index([('age',-1)],name = 'Age')
# print(index_name)

#创建其他类型索引
# myset.create_index([('name',1),('age',1)],sparse=True,unique = True)


# myset.drop_index('name_1')
#删除所有索引
# myset.drop_indexes()    
# #查看索引
# for i in myset.list_indexes():
#     print(i)

#聚合操作
# lst = [{'$group':{'_id':'$gender','num':{'$sum':1}}}]
# cursor = myset.aggregate(lst)
# for i in cursor:
#     print(i)

# myset.delete_many({'gender':{'$exists':False}})
# myset.update_many({},{'$push':{'score':{'$each':[{'English':random.randint(60,100)},
# {'math':random.randint(60,100)},{'Chinese':random.randint(60,100)}]}}})
# cursor = myset.aggregate([{'$project':{'_id':0}},{'$match':{'gender':'w'}},{'$sort':{'score[0]':1}}])
# for i in cursor:
#     print(i)

conn.close()