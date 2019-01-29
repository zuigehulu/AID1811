num = input("请输入您要转换的数:")
num1 = num
jinzhi = int(input("请输入您要转换的进制："))
sum1 = 0
while num != "":
    sum1 = sum1 * jinzhi +ord(num[0])-ord('0')
    num = num[1:]
print(sum1)

sum2 = int(num1,base = jinzhi)
print(sum2)