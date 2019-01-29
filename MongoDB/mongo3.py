from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)

db=conn.image

myset = db.boy

# #读取文件
# with open('random.html','rb') as f:
#     data = f.read()

# #转换mongo格式
# content = bson.binary.Binary(data)

# #讲内容插入集合
# doc = {'file':'random.html','date':content}
# myset.insert_one(doc)
#******************************************************

img = myset.find_one({'file':'random.html'})
#写入本地
with open('random.html','wb') as f:
    f.write(img['date'])
conn.close()