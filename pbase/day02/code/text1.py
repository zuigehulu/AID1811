#  北京出租车计价器
#     收费标准:
#       1. 3公里以内收费 13元
#       2. 基本单价 2.3 元/公里(超过3公里以外)
#       3. 空驶费: 超过15公里后,每公里加收单价的50%空驶费
#          (即3.45元/公里)
#     要求: 输入公里数,打印出费用金额(以元为单位精确到分
money = float(input("请输入公里数"))
money_1 = 0
if money >= 3:
    money_1 = 13 + 2.3 *int((money - 3+1))
    if money >= 15:
        money_1 = money_1 + ((money-15+1) )* 3.45 + (money-15+1) *2.3
        d = round(money_1,2)
        print("金额为:",d,"元")
    else:
        d = round(money_1,2)
        print("金额为:",d,"元")
else:
    print("金额为:13元")

               
