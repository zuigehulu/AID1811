# 写一个程序，实现文件的复制，（注：只复制文件，不复制文件夹）
# 要求１．要考虑文件的关闭问题
# 　　２．要考虑超大文件无法一下加载到内存的问题
# 　　３．要能复制二进制文件
import sys
d = input("请输入要打开的文件:")
num = d.find('.')
d1 = d[:num]+'1'+d[num+1:]
try:
    du = open(d,'rb')
    xie = open(d1,'wb')
    L = du.readlines()
    xie.writelines(L)
except OSError:
    print('文件失败')
finally:
    du.close()
    xie.close()