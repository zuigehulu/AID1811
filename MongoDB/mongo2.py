from pymongo import MongoClient
from random import randint

conn = MongoClient('localhost',27017)

db=conn.stu

myset = db.class0

myset.delete_many({'gender':{'$exists':False}})
cursor = myset.find()
for i in cursor:
    myset.update_one({'_id':i['_id']},{'$set':{'score':{'chinese':randint(60,100),'math':randint(60,100),'english':randint(60,100)}}})
l = [{'$match':{'gender':'w'}},{'$sort':{'score.english':-1}},{'$project':{'_id':0}}]
cursor = myset.aggregate(l)
for i in cursor:
    print(i)

conn.close()