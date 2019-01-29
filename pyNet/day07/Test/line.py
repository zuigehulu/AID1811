from test import *
import time

t = time.time()
#CPU密集型
# for i in range(10):
#     count(1,1)
# print("Line cpu:",time.time()-t)

#IO密集型
for i in range(10):
    write()
    read()
print("Line cpu:",time.time()-t)