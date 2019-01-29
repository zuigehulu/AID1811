# 定义一个变量　money = '人民币１００万元'
# 请打印以下money的长度
# 判断字符串是否全是数字
# 获取万字的索引位置
money = "人民币100万元"
changdu = len(money)
panduan = money.isdigit()
wan = money.find("万")

panduan = "是" if money.isdigit() else "不是"
print("字符串",panduan,"全为数字")
weizhi = money.find("万")
print("万在第",weizhi,"的位置")