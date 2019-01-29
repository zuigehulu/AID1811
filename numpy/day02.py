import numpy as np
a = np.array([[2,23,4],
              [3,32,4]])  #二维矩阵

g = np.array([1,2,3],dtype = float) #定义array的类型是float还是int 默认为int６４　
print(g.dtype)
print(a)
b = np.zeros( (3,4) ) #全部为０的矩阵,3行４列

print(b)
c = np.ones( (3,4)) #全部为１的矩阵，３行４列
print(c)
d = np.empty( (3,4)) # 空的矩阵，一般为0
print(d)
e = np.arange(12).reshape((3,4)) #生成一个有序的数列或矩阵  reshape重新生成
print(e)
#生成一个线段   注意：当生成一个矩阵时，必须保证数字个数符合矩阵的size
f = np.linspace(1,10,6).reshape((2,3))
print(f)